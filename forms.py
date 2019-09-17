from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField,
                     PasswordField, RadioField, IntegerField)

from wtforms.validators import (InputRequired,
                                Length, Email, EqualTo)

from customValidators import (checkForJunk,Age,
                              StrongPassword, isUser, isUser2)


class Login(FlaskForm):

    email = StringField(validators=[
                            InputRequired(
                                'Please Enter your Username Or Email'),
                            Length(min=4, max=50,
                                   message='Invalid Username'), isUser2],
                        render_kw={"placeholder": "Email or Username"})

    password = PasswordField(validators=[
                                 InputRequired('Please Enter your Password'),
                                 Length(min=6, max=16,
                                        message='Invalid Password')],
                             render_kw={"placeholder": "Password"})

    submit = SubmitField("Login",
                         validators=[
                             InputRequired()
                         ])


class Register(FlaskForm):
    name = StringField(validators=[
                           InputRequired('Please Enter your Name'),
                           checkForJunk, Length(min=5, max=20)
                       ], render_kw={"placeholder": "Full Name"})

    email = StringField(validators=[
                            InputRequired('Please Enter your Email'),
                            Email('Please Enter a valid email address'),
                            isUser
                        ], render_kw={
                            "placeholder": "Email Address"})

    username = StringField(
                           validators=[
                               InputRequired('Please Enter your Email'),
                               checkForJunk, isUser
                           ], render_kw={
                               "placeholder": "Username"})

    password = PasswordField(validators=[
                                 InputRequired('Please Enter your Password'),
                                 Length(min=8, max=16,
                                        message='Password Must be 8-16\
 Characters Long'), StrongPassword],
                             render_kw={"placeholder": "Password"})

    password2 = PasswordField(validators=[
                                  InputRequired(
                                      'Please Re-Enter your Password'),
                                  EqualTo('password', 'Password D\
oes Not Match')],
                              render_kw={"placeholder": "Retype Password"})

    gender = RadioField("Gender",
                        choices=[
                            ('M', 'Male'),
                            ('F', 'Female'),
                            ('O', 'Other')],
                        validators=[
                            InputRequired('Please Select a Gender')
                        ])

    age = IntegerField(validators=[
                       InputRequired('Please Enter a Valid Age'), Age],
                       render_kw={
        "placeholder": "Age"})

    submit = SubmitField("Register",
                         validators=[
                             InputRequired()
                         ])
