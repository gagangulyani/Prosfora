from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField,
                     PasswordField, RadioField, IntegerField)
from flask_wtf.file import FileField, FileRequired, FileAllowed
from models.user import User
from models.database import Database
from wtforms.validators import (InputRequired,
                                Length, Email, EqualTo)
from customValidators import (checkForJunk,
                              StrongPassword, isUser, isUser2)
import re


class Login(FlaskForm):

    email = StringField(validators=[
        InputRequired(
            'Please Enter your Username Or Email'),
        Length(min=4, max=50,
               message='Invalid Username'), isUser2],
        render_kw={"placeholder": "Email or Username"})

    password = PasswordField(validators=[
        InputRequired('Please Enter your Password')],
        render_kw={"placeholder": "Password"})

    submit = SubmitField("Login",
                         validators=[
                             InputRequired()
                         ])

    def validate(self):
        rv = FlaskForm.validate(self)
        if not rv:
            return False
        Database.initialize('Prosfora')
        if len(self.password.data) > 16:
            return None
        else:
            result = User.login(self.email.data, self.password.data)

        if result is None:
            self.email.errors = ['Account Not Found!']
            return False

        elif result is False:
            self.password.errors.append('Incorrect Password!')
            return False

        else:
            return result


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

    # about to be depreciated
    gender = RadioField("Gender",
                        choices=[
                            ('M', 'Male'),
                            ('F', 'Female'),
                            ('O', 'Other')],
                        validators=[
                            InputRequired('Please Select a Gender')
                        ])

    submit = SubmitField("Register",
                         validators=[
                             InputRequired()
                         ])


class VideoUpload(FlaskForm):
    file = FileField('Select Video', validators=[
        FileRequired('No Video selected!'),
        FileAllowed(['mp4'], 'MP4 Format Supported Only!')
    ])
    title = StringField(
        validators=[
            InputRequired('Please Enter a title'),
            Length(min=5)
        ],
        render_kw={"placeholder": "Video Title"}
    )

    description = StringField(
        render_kw={"placeholder": "Video Description (optional)"})

    submit = SubmitField("Upload", validators = [InputRequired()])
    

class AudioUpload(FlaskForm):
    file = FileField('Select an Audio', validators=[
        FileRequired('No Audio selected!'),
        FileAllowed(['mp3','wav'], 'Only MP3s and WAVs supported!')
    ])
    title = StringField(
        validators=[
            InputRequired('Please Enter a title'),
            Length(min=4)
        ],
        render_kw={"placeholder": "Audio Title"}
    )

    description = StringField(
        render_kw={"placeholder": "Describe your Audio File (optional)"})

    AlbumArt = FileField('Select an Album Art (optional)', validators=[
        FileAllowed(['jpg', 'png', 'jpeg'], 'Image Files only!')
    ])
    
    submit = SubmitField("Upload", validators = [InputRequired()])
    

class PictureUpload(FlaskForm):
    file = FileField('Select Picture', validators=[
        FileRequired('No Picture selected!'),
        FileAllowed(['jpg', 'png', 'jpeg'], 'Only JPG, PNG and JPEG are supported!')
    ])
    title = StringField(
        validators=[
            InputRequired('Please Enter a title'),
            Length(min=5)
        ],
        render_kw={"placeholder": "Picture Title"}
    )

    description = StringField(
        render_kw={"placeholder": "Describe your Picture (optional)"})
    
    submit = SubmitField("Upload", validators = [InputRequired()])
