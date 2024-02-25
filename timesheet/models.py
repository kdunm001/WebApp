from django.db import models
from core.models import User

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

    # kdb: Meta needed to use external database
    # class Meta:
    #   app_label = 'SFDC' (specify the app label for the external database)
    #   db_table = 'SFDC_locations' (specify the table name in the external database)


class Doctor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return (f"{self.first_name} {self.last_name}")
    

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
    location = models.CharField(max_length=255, null=True, blank=True)
    doctor = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return (f"{self.user} on {self.date} clocked in at {self.clock_in} near {self.location}")

# Team should be linked to a user profile
    # id (primary key)
    # name
    # date created
    # organizer