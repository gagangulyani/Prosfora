from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class register(FlaskForm):
    name = StringField('Name')
    city = StringField('City')
    number = StringField('Contact Number')
    email = StringField('Email')
    password = StringField('Password')
    cpassword = StringField('Confirm Password')
    submit = SubmitField('Register')