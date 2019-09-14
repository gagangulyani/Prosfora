def checkForJunk(form = None, field = None, usrtext= None):
    punct = punctuation.replace('_', '')
    if not field:
        field = {'data': usrtext}
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