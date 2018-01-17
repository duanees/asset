from flask_wtf import FlaskForm
from wtforms.validators import Required, Length, Email,DataRequired
from wtforms import StringField, PasswordField, BooleanField, SubmitField

class LoginForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in',default=False)
    submit = SubmitField('Log In')
