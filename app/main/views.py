from . import main
from flask import render_template,request,redirect,url_for,abort,flash
from ..models import User,Pitch
from .forms import PitchForm, UpdateProfile
from .. import db,photos
from flask_login import login_required,current_user

@main.route('/')
def pitch(title):

    '''
    View movie page function that returns the movie details page and its data
    '''
    pitches = Pitch.get_pitches(title)
    title = 'Home'
    return render_template('index.html',pitches = pitches,title = title)

@main.route('/Pitch/upload',methods = ['GET','POST'])
@login_required
def new_pitch():
    
    form = PitchForm()

    if form.validate_on_submit():
        
        title = form.title.data
        content = form.content.data
        category = form.category.data
        pitch = Pitch(title = title,content = content,category = category)
        
        # Updated pitch instance
        new_pitch = Pitch(title = title,content = content,user = current_user)
            
        # save review method
        new_pitch.save_pitch()
        flash('Your pitch has been created','Success')
        return redirect(url_for('index',id = pitch.id ))
        
    title = 'New Post'
    return render_template('new_pitch.html',title = title,pitch_form = form)

    
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
