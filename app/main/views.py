from . import main
from flask import render_template,request,redirect,url_for,abort,flash
from ..models import User,Pitch,Comment
from .forms import PitchForm,CommentForm,UpdateProfile
from .. import db,photos
from flask_login import login_required,current_user
import markdown2

@main.route('/')
def pitch():

    
    titles = 'Home of The best Pitches'
    return render_template('index.html',title = titles)

@main.route('/Pitch/upload',methods = ['GET','POST'])
@login_required
def new_pitch():
    
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        category = form.category.data
        
        # Updated pitch instance
        new_pitch = Pitch(title = title,category = category,content = content)
            
        # save review method
        new_pitch.save_pitch()
        flash('Your pitch has been created.','Success')
        return redirect(url_for('main.new_comment',id = new_pitch.id))
        
    titles = 'New Post'
    return render_template('new_pitch.html',title = titles,pitch_form = form)


@main.route('/pitch/comment/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_comment(id):
    form = CommentForm() 

    if form.validate_on_submit():
        comment_content = form.comment.data

        comment = Comment(comment_content = comment_content,pitch_id = id)

        comment.save_comment()
        return redirect(url_for('main.index',id = comment.id))
    comment = Comment.query.filter_by(pitch_id = id).all()

    return render_template('new_comment.html',comment = comment,comment_form = form)


@main.route('/comment/<int:id>')
def single_comment(id):
    comment = Comment.query.filter_by(pitch_id = id).all()
    if comment is None:
        abort(404)
    format_comment = markdown2.markdown(comment.comment_content, extras=["code-friendly","fenced-code-blocks"])
    return render_template('comment.html',comment = comment,format_comment = format_comment)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    title = f"{uname}'s profile page"
    return render_template("profile/profile.html", user = user, title = title)


@main.route('/user/<uname>/update/bio',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    title = 'Update bio'
    return render_template('profile/update.html',form =form,title = title)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))
