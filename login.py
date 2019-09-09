from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class login(FlaskForm):
    
    email = StringField('Email')
    password = StringField('Password')
    submit = SubmitField('Login')