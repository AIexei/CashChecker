from django import forms
from .validators import *


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'password')


    username = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'finput',
        'placeholder': 'Your email'
    }), required=True, validators=[email_validator])


    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your name'
    }), required=True, validators=[name_validator])


    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter password',
    }), required=True, validators=[password_validator])


    cpsw = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'linput',
        'placeholder': 'Confirm password',
    }), required=True)


    def send_email(self):
        pass


    def clean(self):
        self.cleaned_data = super(RegisterForm, self).clean()

        if self.cleaned_data.get('cpsw') != self.cleaned_data.get('password'):
            raise ValidationError('Passwords don\'t match.')

        return self.cleaned_data


    def save(self, commit=False):
        print('RegisterForm.save()')

        new_user = super(RegisterForm, self).save(commit=False)
        new_user.set_password(self.cleaned_data['password'])
        return new_user.save()


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

    # email maxlength = 150
    # name maxlength = 30
    # pass min = 8 max = 30