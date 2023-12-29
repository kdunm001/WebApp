from django.db import models
from core.models import User

# Create your models here.
# Timesheet should be linked to Userprofile
class Timesheet(models.Model):
    # id (primary key, auto-generated)
    # kdb: on_delete=models.CASCADE (if User is deleted, the timesheet will also be deleted)
    # kdb: other option, on_delete=models.SET_NULL, null=True will set the user_id to NULL
    # kdb: another option, on_delete=models.SET_DEFAULT, null=True, defaul=XXX will set the user_id to whatever is specified as the default value
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    clock_in = models.TimeField(null=True, blank=True)
    clock_out = models.TimeField(null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)
    # location = models.CharField(max_length=255, null=True, blank=True)

# Team should be linked to a user profile
    # id (primary key)
    # name
    # date created
    # organizer