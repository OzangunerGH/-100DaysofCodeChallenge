from wtforms import StringField, SubmitField, PasswordField
from flask_wtf import FlaskForm
from wtforms.validators import *


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class UserForm(FlaskForm):
    name = StringField("Full Name", validators=[DataRequired()])
    email = StringField("Email address", validators=[DataRequired(), Email()])
    password = PasswordField("Password",
                             validators=[DataRequired(), EqualTo('confirm', message="Passwords must match.")])
    confirm = PasswordField("Confirm Password", validators=[DataRequired()])
    submit = SubmitField('Register')
