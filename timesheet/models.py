from django.db import models

# Create your models here.
# Timesheet should be linked to Userprofile
    # id (primary key)
    # kdb: on_delete=models.CASCADE (if userprofile is deleted, the timesheet will also be deleted)
    # kdb: other option, on_delete=models.SET_NULL, null=True will set the user_id to NULL
    # kdb: another option, on_delete=models.SET_DEFAULT, null=True, defaul=XXX will set the user_id to whatever is specified as the default value
    # user_id = models.ForeignKey("Userprofile", on_delete=models.CASCADE) (foreign key, from Userprofile)
    # datetime of start
    # datetime of end
    # duration between start and end
    # location (foreign key, from Locations)

# Query the database with a year greater than 2021
# Timesheet.objects.filter(year__gt=2021)