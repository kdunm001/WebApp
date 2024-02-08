# kdb: Creating custom UserCreation form, that will use my custom User model, instead of the default User model from Django
# Noticed that UserCreationForm inherits from BaseUserCreationForm - need to override the Meta User model in the BaseUserCreationForm
# from django.contrib.auth.forms import BaseUserCreationForm, UsernameField - THIS DID NOT WORK
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email',)