# kdb: This .py file helps handle web requests (i.e. redirect, etc.)

from django.shortcuts import render, redirect
# Django's generic, pre-based class views that can be inherited
# from django.views.generic import TemplateView

# Create your views here.
# kdb: Django will supply the "request" to this function when a user goes to a specific page on the website

# Function-base view
def home_page(request):
    return render(request, "core/home_page.html")

# Class-based view
# class HomePageView(TemplateView):
#     template_name = "core/home_page.html"