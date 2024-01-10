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

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-n%a^rihqiv5y8i05ani90w0hr-)g1%uy@r6*khuh!i8ra=$pip'
GOOGLE_MAPS_API_KEY = 'AIzaSyCbJteY-0D9_W3lwHCzv4GJ8IKRBjOCiE0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# kdb: In production, this is where the hosts will be identified.  For local development, this can be left blank.
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # kdb: Django's default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # kdb: Third-party apps
    'crispy_forms',
    'crispy_tailwind',

    # kdb: Locally created apps
    'core',
    'timesheet',
]

MIDDLEWARE = [
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
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
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

STATIC_URL = 'static/'
# kdb: Extra static settings, lists of paths to help Django recognize static files
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
# kdb: Root folder for all static files, once all items are placed in one directory
STATIC_ROOT = "static_root"

# kdb: Imaves and videos location
MEDIA_URL = 'images/'


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# kdb: Telling Django that I have a custom User model
AUTH_USER_MODEL = 'core.User'

# kdb: Overriding the defaul login and logout redirects
LOGIN_REDIRECT_URL = "home_page"
LOGOUT_REDIRECT_URL = "home_page"

# kdb: Configure email backend, telling Django how to send emails, in the instance below, it just logs the emails in the terminal - will need to be updated for production
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# kdb: What is used by default is smtp (simple Mail Transfer Protocol), and needs configuration with smtp credentials (which is given by email providers like SendGrid or MailGun)
# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# OR
# EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
# EMAIL_FILE_PATH = BASE_DIR / "sent_emails"


# kdb: Linking Crispy Forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"
CRISPY_TEMPLATE_PACK = "tailwind"