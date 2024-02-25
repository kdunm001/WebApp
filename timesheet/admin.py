from django.contrib import admin
from .models import Timesheet, Location, Doctor

# Register your models here.
admin.site.register(Timesheet)
admin.site.register(Location)
admin.site.register(Doctor)