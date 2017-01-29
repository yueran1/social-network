from flask_wtf import Form
from wtforms import StringField, TextAreaField, BooleanField, SelectField,\
SubmitField
from wtforms.validators import Required, Length, Email, Regexp
from wtforms import ValidationError
from flask_pagedown.fields import PageDownField
from ..models import Role, User
from flask_login import login_user, login_required, logout_user, current_user

#Required() validator ensures that the field is not submitted empty	
class NameForm(Form):
	name=StringField('What is your name?', validators=[Required()])
	submit= SubmitField('Submit')
	
class EditProfileForm(Form):
	name = StringField('Real name', validators=[Length(0, 64)])
	location = StringField('Location', validators=[Length(0,64)])
	about_me = TextAreaField('About me')
	submit = SubmitField('Submit')
