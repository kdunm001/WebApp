from django.contrib import admin
from .models import Timesheet, Location

# Register your models here.
admin.site.register(Timesheet)
admin.site.register(Location)