# kdb: Creating custom UserCreation form, that will use my custom User model, instead of the default User model from Django
# Noticed that UserCreationForm inherits from BaseUserCreationForm - need to override the Meta User model in the BaseUserCreationForm
# from django.contrib.auth.forms import BaseUserCreationForm, UsernameField - THIS DID NOT WORK
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {"username": UsernameField}