# kdb: This .py file helps handle web requests (i.e. redirect, etc.)

# kdb: Import used to send emails
from django.core.mail import send_mail
# kdb: Django automatically imports render, I aded redirect and reverse
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

# kdb: Django already has LoginView, LogoutView, and PasswordResetView, so no need to create
# kdb: Django does not have a pre-build SignupView, so I have created one below

class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")
    
    def form_valid(self, form):
        # Get the user instance without saving it to the database yet
        user = form.save(commit=False)

        # Additional fields not included in the form (email, first_name, last_name)
        user.email = form.cleaned_data['email']
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        

        # Save the user with the additional fields
        user.save()

        # TODO send email
        # send_mail(
        #     subject="Signup confirmed!",
        #     message="Thank you for signing up!",
        #     from_email="noreply@test.com",
        #     recipient_list="test@test.com"
        # )

        # kdb: super() function inherits from SignupView to continue it's functionality, allows me to add items within the SignupView process
        return super(SignupView,self).form_valid(form)