from django.core.exceptions import ValidationError
import re


def validate_password(value):
    if len(value) < 8:
        raise ValidationError('Short password.')
    elif len(value) > 30:
        raise ValidationError('Long password.')
    elif not re.match(r'^[\d|a-zA-Z]{8,30}$', value):
        raise ValidationError('Invalid password.')

    print('there')

    return value