from django.core.validators import ValidationError
from django.contrib.auth.models import User
import re


def email_validator(email):
    if len(email) > 150:
        raise ValidationError('Very long email.')
    elif User.objects.filter(username__iexact=email).exists():
        raise ValidationError('User with that email exists.')

    return email


def name_validator(name):
    if len(name) > 30:
        raise ValidationError('Very long name.')

    return name


def password_validator(psw):
    if len(psw) < 8:
        raise ValidationError('Short password.')
    elif len(psw) > 30:
        raise ValidationError('Long password.')
    elif not re.match(r'^[\d|a-zA-Z]{8,30}$', psw):
        raise ValidationError('Invalid password.')

    return psw


def confirmed_password_validator(psw, cpsw):
    if psw != cpsw:
        raise ValidationError('Passwords don\'t match.')

    return psw