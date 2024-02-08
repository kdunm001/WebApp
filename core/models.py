# kdb: Models is a representation of the database schema

from django.db import models
# kdb: Django has built in functionalities to assist with authentication via User model
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from webapp_django.managers import CustomUserManager


# Create your models here.
# kdb: class inherts from .Model to identify that it is now a model for the database
# Custom User model instructions from https://testdriven.io/blog/django-custom-user-model/

# kdb: Per Django documentation, it is recommended to create a custom User model
# kdb: Inheriting from Django's pre-built AbstractUser model
class User(AbstractUser):
    # Already includes the following, username and password are required
    username = None
    email = models.EmailField(max_length=150, unique=True)
    # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)
    # is_staff (BooleanField, default=False)
    # is_active (BooleanFIeld, default=True)
    # date_joined (DateTimeField, default=timezone.now)

    # Set email as the unique identifier for authentication
    USERNAME_FIELD = 'email'

    # Specify which fields are required when creating a superuser
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return (f"{self.email}, {self.first_name} {self.last_name}")