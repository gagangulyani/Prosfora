from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField,
                     PasswordField, RadioField, IntegerField)

from wtforms.validators import (InputRequired,
                                Length, Email, EqualTo)

from customValidators import (checkForJunk,
                              StrongPassword, isUser, isUser2)


class Login(FlaskForm):

    email = StringField("Email/Username",
                        validators=[
                            InputRequired(
                                'Please Enter your Username Or Email'),
                            Length(min=4, max=50,
                                   message='Invalid Username'), isUser2],
                        render_kw={"placeholder": "Martha_Jones96"})

    password = PasswordField("Password",
                             validators=[
                                 InputRequired('Please Enter your Password'),
                                 Length(min=6, max=16,
                                        message='Invalid Password')],
                             render_kw={"placeholder": "******"})

    submit = SubmitField("Login",
                         validators=[
                             InputRequired()
                         ])


class Register(FlaskForm):
    name = StringField("Full Name",
                       validators=[
                           InputRequired('Please Enter your Name'),
                           checkForJunk, Length(min=5, max=20)
                       ], render_kw={"placeholder": "Your Name"})

    email = StringField("Email",
                        validators=[
                            InputRequired('Please Enter your Email'),
                            Email('Please Enter a valid email address'),
                            isUser
                        ], render_kw={
                            "placeholder": "Your Email Address"})

    username = StringField("Username",
                           validators=[
                               InputRequired('Please Enter your Email'),
                               checkForJunk, isUser
                           ], render_kw={
                               "placeholder": "Choose a Username"})

    password = PasswordField("Password",
                             validators=[
                                 InputRequired('Please Enter your Password'),
                                 Length(min=8, max=16,
                                        message='Password Must be 8-16\
 Characters Long'), StrongPassword],
                             render_kw={"placeholder": "******"})

    password2 = PasswordField("Confirm Password",
                              validators=[
                                  InputRequired(
                                      'Please Re-Enter your Password'),
                                  EqualTo('password', 'Password D\
oes Not Match')],
                              render_kw={"placeholder": "******"})

    gender = RadioField("Gender",
                        choices=[
                            ('M', 'Male'),
                            ('F', 'Female'),
                            ('O', 'Other')],
                        validators=[
                            InputRequired('Please Select a Gender')
                        ])

    age = IntegerField('Age', validators=[
                       InputRequired('Please Enter a Valid Age')],
                       render_kw={
        "placeholder": "23"})

    submit = SubmitField("Register",
                         validators=[
                             InputRequired()
                         ])
