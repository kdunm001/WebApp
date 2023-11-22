# kdb: This .py file helps with administrative tasks (i.e. runserver and database migrations)

#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


# kdb: Setting the default environment variable (DJANGO_SETTING_MODULE, which is the webapp_django.settings path), and tries to execute a command given the system arguments (using imported sys library)
def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webapp_django.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
