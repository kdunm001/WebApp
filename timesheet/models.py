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
    # kdb: active field added to help identify if a user has already clocked in (I am noticing that once a user clocks in, if they visit another page, the clocked in status is not saved, and they are asked to clock in again)
    active = models.BooleanField(default=False)
    # kdb: latitude and longitude added to document the user's location, max_digits=9 and decimal_places=6 will help store the user's precise location.
    clock_in_latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    clock_in_longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    clock_out_latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    clock_out_longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

# Team should be linked to a user profile
    # id (primary key)
    # name
    # date created
    # organizer