from string import punctuation
from wtforms.validators import ValidationError
from models.user import User
from models.database import Database
from PIL import Image
from magic import Magic
from os import remove, stat, listdir
from copy import deepcopy
import re


def cleanup():
    for i in listdir():
        if 'temp.' in i[:5]:
            remove(i)
            print(i, 'deleted!')
            
def checkForJunk(form=None, field=None, usrtext=None):
    punct = punctuation.replace('_', '')
    if not field:
        class a:
            def __init__(self, data):
                self.data = data

        field = a(usrtext)

    for i in field.data:
        if i in punct:
            if usrtext:
                return True
            else:
                raise ValidationError(
                    'Only Alphabets, Numbers and Underscores Allowed!')


def StrongPassword(form, field):
    punct = punctuation
    numbers = "0123456789"
    alphabets = "QWERTYUIOPASDFGHJKLZXCVBNM"

    errors = {
        "isSpecial": 'Special Symbol',
        "isNumber": 'Number',
        'isUpper': 'UpperCase Character'
    }

    if any(char in field.data for char in punct):
        errors.pop('isSpecial')

    if any(char in field.data for char in numbers):
        errors.pop('isNumber')

    if any(char in field.data for char in alphabets):
        errors.pop('isUpper')

    if errors:
        message = "Password Must Contain atleast 1 "
        errors = [errors[msg] for msg in errors]
        extra = ", ".join(errors[:-1])
        if extra:
            extra2 = " and " + errors[-1]
        else:
            extra2 = errors[-1]

        message += extra + extra2

        raise ValidationError(message)


def isUser(form, field, login=False):
    Database.initialize('Prosfora')
    email = field.data.lower()
    isEmail = re.compile(r"[^@]+@[^@]+\.[^@]+")

    if len(email) > 100:
        raise ValidationError('Email or Username is too lengthy!')

    if isEmail.fullmatch(email):
        isUser_ = User.isUser(email=email)
        email = True
    else:
        isUser_ = User.isUser(username=email)
        email = False

    print(isUser_)

    if login:
        if not isUser_:
            raise ValidationError('Account Does Not exist!')

    else:
        if isUser_:
            if email:
                raise ValidationError('Email Already Taken!')
            raise ValidationError('Username Already Taken!')


def isUser2(form, field):
    isUser(form, field, login=True)


def imageValidator(form, field):
    
    f = field.data
    temp = deepcopy(f)
    try:
        img = Image.open(temp)
        img.verify()

    except IOError:
        raise ValidationError('Image is Invalid or Corrupt!')


def videoValidator(form, field):
    f = field.data
    fname = f"temp.{f.filename.split('.')[-1]}"
    f.save(fname)
    file_size = (stat(fname).st_size / 1024) / 1024
    type_ = Magic(mime=True).from_file(fname)
    cleanup()
    if 'video' not in type_:
        raise ValidationError('Only Vidoe files are supported!')

    isExt = False
    for i in ['mp4', 'mov', 'webm', 'flv', 'quicktime']:
        if i in type_:
            isExt = True
            break

    if not isExt:
        raise ValidationError(type_)

    if file_size > 200:
        raise ValidationError('Video File Too Large! (Video > 200MB)')


def audioValidator(form, field):

    f = field.data
    fname = f"temp.{f.filename.split('.')[-1]}"
    f.save(fname)
    file_size = (stat(fname).st_size / 1024) / 1024
    type_ = Magic(mime=True).from_file(fname)
    cleanup()
    if 'audio' not in type_ and 'x-font-gdos' not in type_:
        raise ValidationError(type_)

    if file_size > 100:
        raise ValidationError('Audio File Too Large! (Audio > 100MB)')

