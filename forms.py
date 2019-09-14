from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired , Length , Email , EqualTo, ValidationError

class Login(FlaskForm):
    
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = StringField('Password',validators=[DataRequired()])
    submit = SubmitField('Login')


class Register(FlaskForm):
    name = StringField('Name',validators=[DataRequired(),Length(min=2,max=20)])
    city = StringField('City',validators=[DataRequired()])
    number = StringField('Contact Number',validators=[DataRequired()])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = StringField('Password',validators=[DataRequired()])
    cpassword = StringField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Register')    