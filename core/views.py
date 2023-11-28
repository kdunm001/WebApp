# kdb: This .py file helps handle web requests (i.e. redirect, etc.)

from django.shortcuts import render, redirect, reverse
# kdb: Django's generic, pre-based class views that can be inherited
# from django.views.generic import TemplateView
# kdb: Imports used to create SignupView
from django.views import generic
from .forms import CustomUserCreationForm

# Create your views here.
# kdb: Django will supply the "request" to this function when a user goes to a specific page on the website

# Function-base view
def home_page(request):
    return render(request, "core/home_page.html")

# Class-based view
# class HomePageView(TemplateView):
#     template_name = "core/home_page.html"

# kdb: Django already has LoginView and LogoutView, so no need to create
# kdb: Django does not have a pre-build SignupView, so I have created one below

class SignupView(generic.CreateView):
    template_name = "core/registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")