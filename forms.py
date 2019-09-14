from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired , Length , Email , EqualTo, ValidationError

class Login(FlaskForm):
    
    email = StringField('Email',validators=[InputRequired(),Email(),Length(min=10,max=25)])
    password = StringField('Password',validators=[InputRequired()],Length(min=8))
    submit = SubmitField('Login')


class Register(FlaskForm):
    name = StringField('Name',validators=[InputRequired(),Length(min=2,max=20)])
    city = StringField('City',validators=[InputRequired()])
    number = StringField('Contact Number',validators=[InputRequired()])
    email = StringField('Email',validators=[InputRequired(),Email()])
    password = StringField('Password',validators=[InputRequired()])
    cpassword = StringField('Confirm Password',validators=[InputRequired(),EqualTo('password')])
    submit = SubmitField('Register')    