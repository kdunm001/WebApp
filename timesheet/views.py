from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import datetime
from .models import Timesheet
#kdb: Verifies that user is authenticated, and, if not authenticated, will redirect the user to the log in screen
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# kdb: Only want the user to view their own information, use mixins (arguments that are added to the inheritance of classes)

# Create your views here.
# Function-base view
def history(request):
    user_timesheets = Timesheet.objects.filter(user=request.user).order_by('-date', '-clock_in')    
    context = {
            "user_timesheets": user_timesheets,
        }
    return render(request, "timesheet/history.html", context)

@login_required
def clock_in(request):  
    # I am having trouble to keep the clocked-in status once a user leaves to another page, a solution is to use session data to store information about whether the user is currently clocked in (that way the database is not constantly queried to check if the user is clocked in)
    if request.method == "POST":
        current_date = timezone.now().date()
        current_time = timezone.now().time()

        # Create a new Timesheet entry with current date and time when clocked in, and set it as active
        timesheet = Timesheet(user=request.user, date=current_date, clock_in=current_time, active=True)
        timesheet.save()

        # Update session data to True
        request.session['clocked_in'] = True

        return redirect('clock_out')
    
    else:
        # Check if the user is already clocked in (using session data)
        if request.session.get('clocked_in', False):
            return redirect('clock_out')
        
        else:
            return render(request, 'timesheet/clock-in.html')


@login_required
def clock_out(request):
    if request.method == "POST":
        # Using the Model Manager, query the database for the latest Timesheet entry for the current user and update the clock_out field
        #timesheet = Timesheet.objects.filter(user=request.user, clock_out__isnull=True).order_by('-date', '-clock_in').first()
        timesheet = Timesheet.objects.filter(user=request.user, active=True).first()

        if timesheet:
            clock_out_date = timezone.now().date()
            timesheet.clock_out = timezone.now().time()
            timesheet.active = False
            
            # Calculate the duration, make sure when subtracting to combine the date and time from the fields that were entered (date and clock_in) when the user clocked in, in order to calculate duration
            timesheet.duration = datetime.combine(clock_out_date, timesheet.clock_out) - datetime.combine(timesheet.date, timesheet.clock_in)
            
            timesheet.save()

            # Update session data to False
            request.session['clocked_in'] = False

            return redirect('clock_in')
        
    return render(request, 'timesheet/clock-out.html')
