from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Profile
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'usernameField form-control','placeholder':"Username","placeholder":"Username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'passwordField form-control','placeholder':'Password', "placeholder":"Password"}))

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Profile
        fields = "__all__"

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Profile
        fields="__all__"
