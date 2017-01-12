from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length

class LoginForm(Form):
	username = StringField('Username', validators=[Required()])
	password = PasswordField('Password', validators =[Required()])
	remember_me = BooleanField('Keep me logged in')
	submit = SubmitField('Log in')
