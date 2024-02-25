# Commands that are going to be run every time the app is deployed

# Collect all static files
python manage.py collectstatic --no-input

# Make sure that the production database has the most up-to-date schema
python manage.py migrate

# See https://docs.digitalocean.com/developer-center/deploy-a-django-app-on-app-platform/
gunicorn --worker-tmp-dir /dev/shm webapp_django.wsgi