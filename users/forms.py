from django import forms
from django.core.validators import validate_email
from .validators import validate_password


'''
class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'finput'
    }), required=True, help_text='Email address', validators=[validate_email,])


    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'linput',
        'name': 'psw'
    }), required=True, help_text=None, validators=[validate_password,])


    # non-field-errors
    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        print('clean')
        return cleaned_data

    - deactivated account
    - invalid data
    
    # field-errors
    def clean_email(self):
        pass
        - email expr do not match
        


    def clean_password(self):
        pass
        - too short
        - too long
        - unavailable symbols
'''


class RegisterForm(forms.Form):
    pass

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()