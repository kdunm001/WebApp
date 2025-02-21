# kdb: This .py file is the hub where settings are held (i.e. global variables, configure database connections and template locations)

"""
Django settings for webapp_django project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
# kdb: Using django-environ docs to assist with creating environment variables that will be hidden during production, https://django-environ.readthedocs.io/en/latest/
import environ
import os

env = environ.Env(
    # Set casting, default value
    DEBUG=(bool, False)
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Set the project base directory, per the environ instructions - this is not working
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Normally, deployment providers allow us to specify environment varibles within the UI when creating a project, and will be loaded in the terminal when the project is being deployed, and set variables in the session
# Environment variables will be read from the session first, not the .env file, since the .env file is only used in local development
# $env:READ_DOT_ENV_FILE=$true (for PowerShell), set READ_DOT_ENV_FILE=True (for Windows), export READ_DOT_ENV_FILE=True (for Unix shells)
READ_DOT_ENV_FILE = env.bool('READ_DOT_ENV_FILE', default=False)
if READ_DOT_ENV_FILE:
    # Take environment variables from .env file
    # kdb: Reading the .env file into project, so we can access variables
    environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# False if not in os.environ because of casting above
DEBUG = env('DEBUG')

# Raises Django's ImproperlyConfigured, exception if SECRET_KEY not in os.environ
SECRET_KEY = env('SECRET_KEY')
GOOGLE_MAPS_API_KEY = env('GOOGLE_MAPS_API_KEY')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/


# Application definition
# kdb: Install django-tailwind and follow the instructions to register tailwind in the django project https://django-tailwind.readthedocs.io/en/latest/installation.html
INSTALLED_APPS = [
    # kdb: Django's default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # kdb: Third-party apps
    'tailwind',
    'theme',
    'crispy_forms',
    'crispy_tailwind',
    "whitenoise.runserver_nostatic",

    # kdb: Locally created apps
    'core',
    'timesheet',
]

TAILWIND_APP_NAME = 'theme'

INTERNAL_IPS = [
    "127.0.0.1",
]

NPM_BIN_PATH = "C:/Program Files/nodejs/npm.cmd"

MIDDLEWARE = [
    #kdb: Added middleware for whitenoise
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # kdb: Django's default middleware
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# kdb: Path to the general urls.py file
ROOT_URLCONF = 'webapp_django.urls'

# kdb: List of configuration objects
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # kdb: Templates can be entered below in the list of directories
        'DIRS': [ BASE_DIR / 'core' / 'templates' ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# kdb: Django automatically points to WSGI to run the application
WSGI_APPLICATION = 'webapp_django.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# kdb: This database configuration can be updated to indicate another type of database, SQLite3 is good for local but not for producation (PostgreSQL or MySQL is recommended).
# 'ENGINE': 'django.db.backends.sqlite3',
# 'NAME': BASE_DIR / 'db.sqlite3',

DATABASES = {
    'default': env.db(),
    
    'extra': env.db_url(
        'DATABASE_URL',
    )
}

# kdb: In order to use an external database for the locations of addresses
# 1. Install the required database connector (i.e. if PostgreSQL, CLI command: pip install psycopg2)
# 2. Adjust database settings (above) to include
# 'default': {
#   'ENGINE': 'django.db.backends.postgresql',
#   'NAME': 'ENTER DATABASE NAME HERE',
#   'USER': 'ENTER DATABASE USER HERE',
#   'PASSWORD': 'ENTER DATABASE PASSWORD HERE',
#   'HOST': 'ENTER DATABASE HOST HERE',
#   'POST': 'ENTER DATABASE PORT HERE',
# }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

# kdb: Password validators can be modified at a later time, but what is provided are default Django settings
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

# kdb: Internationalization
USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
# kdb: Extra static settings, lists of paths to help Django recognize static files
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
# kdb: Root folder for all static files, once all items are placed in one directory
STATIC_ROOT = "static_root"

# kdb: Images and videos location
MEDIA_URL = '/images/'

# kdb: Add configuration to whitenoise
STORAGES = {
    # ...
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# kdb: Telling Django that I have a custom User model
AUTH_USER_MODEL = 'core.User'

# kdb: Overriding the defaul login and logout redirects
LOGIN_REDIRECT_URL = 'home_page'
LOGOUT_REDIRECT_URL = 'home_page'

# kdb: Configure email backend, telling Django how to send emails, in the instance below, it just logs the emails in the terminal - will need to be updated for production
#EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# kdb: What is used by default is smtp (Simple Mail Transfer Protocol), and needs configuration with smtp credentials (which is given by email providers like SendGrid or MailGun)
# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# OR
# EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
# EMAIL_FILE_PATH = BASE_DIR / "sent_emails"

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_HOST_USER = 'postmaster@sandbox15e019de97b74827910a1bf6d3659f3f.mailgun.org'
EMAIL_HOST_PASSWORD = 'f4cf3b22b8234b903a3ca0e4bac6955d-8c8e5529-748ea16a'
# TLS is for secure email sending
EMAIL_USE_TLS = True
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = 'noreply@spacetrace.com'

# kdb: Linking Crispy Forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"
CRISPY_TEMPLATE_PACK = "tailwind"

# When in production, here are the security settings
if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_HSTS_SECONDS = 31536000 # 1 year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    X_FRAME_OPTIONS = "DENY"

# kdb: In production, this is where the hosts will be identified.  For local development, this can be left blank. the "*" allows this app to work on any host website.
ALLOWED_HOSTS = ["spacetrace-app-59mhc.ondigitalocean.app", "*"]

