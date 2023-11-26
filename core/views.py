# kdb: This .py file helps handle web requests (i.e. redirect, etc.)

from django.shortcuts import render

# Create your views here.
# kdb: Django will supply the "request" to this function when a user goes to a specific page on the website
def home_page(request):
    return render(request, "core/home_page.html")