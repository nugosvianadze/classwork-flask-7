from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField


class LoginForm(FlaskForm):
    email = EmailField('Email')
    password = PasswordField('Password')
    submit = SubmitField()


class RegisterForm(LoginForm):
    username = StringField('Username')
