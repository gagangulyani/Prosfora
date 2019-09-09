from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class LoginForm(FlaskForm):
    
    email = StringField('Email')
    password = StringField('Password')
    submit = SubmitField('Login')


class Join(FlaskForm):
    name = StringField('Name')
    city = StringField('City')
    number = StringField('Contact Number')
    email = StringField('Email')
    password = StringField('Password')
    cpassword = StringField('Confirm Password')
    submit = SubmitField('Register')    