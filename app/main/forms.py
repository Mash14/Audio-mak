from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.fields.core import SelectField
from wtforms.validators import Required

class PitchForm():
    title = StringField('Pitch Title',validators = [Required()])
    category = SelectField('Pitch Category', choices=[('Select a category','Select Pickup lines','Select Interview Pitch')])
    content = TextAreaField
    submit = 'Post'


class CommentForm(FlaskForm):
    comment = TextAreaField('Post of the comment')
    submit = SubmitField('Submit')

    
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')