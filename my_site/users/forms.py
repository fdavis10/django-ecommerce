from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'password']

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        )

        first_name = forms.CharField()
        last_name = forms.CharField()
        email = forms.CharField()
        password1 = forms.CharField()
        passwords2 = forms.CharField()

class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email'
        )

        first_name = forms.ImageField()
        last_name = forms.ImageField()
        username = forms.ImageField()
        email = forms.ImageField()