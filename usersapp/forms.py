from django import forms
from usersapp.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields = [
            'first_name',
            'username',
            'email',
            'password1',
            'password2',
            'phone',
            'role'
        ]

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())