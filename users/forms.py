from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'password')

    email = forms.EmailField(required=True, help_text=None)
    first_name = forms.CharField(required=True, help_text=None, max_length=30)
    password = forms.CharField(max_length=20, required=True, widget=forms.PasswordInput())
    confirm_password = forms.CharField(max_length=20, required=True, widget=forms.PasswordInput())