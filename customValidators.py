from string import punctuation
from wtforms.validators import ValidationError
from models.user import User
from models.database import Database
import re


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
                raise ValidationError('Email Already Taken')
            raise ValidationError('Username Already Taken')


def isUser2(form, field):
    isUser(form, field, login=True)
