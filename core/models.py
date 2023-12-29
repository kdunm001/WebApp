# kdb: Models is a representation of the database schema

from django.db import models
# kdb: Django has built in functionalities to assist with authentication via User model
from django.contrib.auth.models import AbstractUser


# Create your models here.
# kdb: class inherts from .Model to identify that it is now a model for the database

# kdb: Per Django documentation, it is recommended to create a custom User model
# kdb: Inheriting from Django's pre-built AbstractUser model
class User(AbstractUser):
    # Already includes the following, username and password are required
    # username (CharField)
    # first_name (CharField)
    # last_name (CharField)
    # email (EmailField)
    # is_staff (BooleanField, default=False)
    # is_active (BooleanFIeld, default=True)
    # date_joined (DateTimeField, default=timezone.now)
    pass

    def __str__(self):
         return User.username