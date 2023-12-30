"""
URL configuration for webapp_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# kdb: Link static folder to URLs
from django.conf import settings
from django.conf.urls.static import static
# kdb: Pre-populated from Django
from django.contrib import admin
from django.urls import path, include
# kdb: Link views to URLs
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from core.views import home_page, SignupView # Class view: HomePageView
from timesheet.views import clock_in, clock_out, history

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home_page'),
    # Class based view path('', HomePageView.as_view(), name="home_page")
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-reset/', PasswordResetView.as_view(), name='password-reset'),
    path('password-reset-done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    # Under venv > django > contrib > auth > views.py is the PasswordResetConfirmView, and in the dispatch function, it needs "uidb64" and "token" in kwargs, which is passed in through the URL
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('clock-in/', clock_in, name='clock_in'),
    path('clock-out/', clock_out, name='clock_out'),
    path('history/', history, name='history')
]

if settings.DEBUG == True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)