from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.fields.core import SelectField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    title = StringField('Pitch Title',validators = [Required()])
    category = SelectField('Pitch Category', choices=[('Select a category','Select a category'),('Select Pickup Lines','Select Pickup Lines'),('Select Interview Pitch','Select Interview Pitch'),('Select Sales Pitch','Select Sales Pitch')])
    content = TextAreaField('Pitch Content',validators = [Required()])
    submit = SubmitField('Post')


class CommentForm(FlaskForm):
    comment = TextAreaField('Post of the comment')
    submit = SubmitField('Submit')

    
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')