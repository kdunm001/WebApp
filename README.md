# SPACE TRACE
### Video Demo: 
https://youtu.be/tQvcdOAoXT0
### Description: 
_This is a location-based timesheet web application._
This is a Python project, using Django web framework, that serves as a timesheet that logs the user's clocked-in time and the location in which they clocked in.  Ideally, this application would clock the user out if they leave a 0.01 radius of their clocked in location (allowing some flexibility to move around in a building or office location, but once they leave the building, they would be clocked out, if the have not clocked out manually).

### File Contents:
Below is a description of each file in the project, what they contain, and what they do (if I created them or understand fully what they do)

**WebApp/**
- **core/**
    - **pycache/** (This folder was automatically generated when I created the core app, I did not touch this folder and the files within)
    - **migrations/** (this filder and files within are created when running the command `python manage.py makemigrations` and executed, mainly to the database schema when running the command `python manage.py migrate`)
    - **templates/** (this folder was created to hold the main html templates for this project)
        - **core/**
            - **base.html** (I created this to be the base layout of the html pages, you will see the opportunity for Jinja insertions throughout this layout)
            - **home_page.html** (I created this to design the home page layout, using Jinja syntax, it inherits from the base.html file and loads a static image)
        - **registration/** (All html files created under this folder are specific to user authentication)
            - **login.html** (I created this html file to allow users to log in, I dabbled with crispy forms to help make the form more visually appealing to the user)
            - **password_reset_complete.html** (I created a simple html file to identify that a user has successfully reset their password)
            - **password_reset_confirm.html** (I created a simple html file to allow a user to enter in a new password, again using crispy forms)
            - **password_reset_done.html** (I created a simple html file to identify that a password reset has been requested by the user, the intent is to have an email sent to the user, but I have yet to apply that feature)
            - **password_reset_email.html** (I created simple language that would be rendered in an email to a user that provides them with a link to reset their password)
            - **password_reset_form.html** (I created a simple html that inquires if a user really wants to reset their password)
    - **init.py** (This file helps register that this directory is a Python package/module)
    - **admin.py** (This file is auto-created when a Django app is initialized, and the information inside allows the admin side to register certain models, for instance, this file helps to register the User model)
    - **apps.py** (This file helps configure this directory/folder (core) as a Django app)
    - **forms.py** (This file helps to identify the forms that will be used on the client-side of the website, using the information that is entered throught the html and saving it to the database)
    - **models.py** (This file help structure the database for this project each model is a representation of the database schema, for instance, I created a custom User model that inherits from the AbstractUser model that is already provided in Django - this will allow me to add fields to the User model, which would be difficulty to do, if I had not created a custom model)
    - **tests.py** (This file was automatically generated when I established the core app and is used to test the code throughout this app; however, I did not edit this file)
    - **views.py** (This file helps handle web requests (i.e. redirect, etc.), and most of the code that I wrote throughout this project lies in the views.py files - this one in particular handles the home page and sign up views, and I experimented with function- and class-based views)
- **static/** (This folder contains all of the static files used throughout this project)
    - **css/** (This folder would contain CSS files, but I chose to utilize Tailwind CSS)
    - **images/** (This folder contains all of the images used throughout this web app)
        - **home_page_graphic.png** (This is an image that I created to be shown on the home_page.html)
        - **space_trace_logo.png** (This is an image that I created to be the website logo, which is displayed in the header in base.html)
    - **javascript/** (This folder would contain JavaScript files, but I chose not to utilize JS across the website, I only used it in the history.html file)
- **timesheet/**
    - **pycache/** (This folder was automatically generated when I created the core app, I did not touch this folder and the files within)
    - **migrations/** (this filder and files within are created when running the command "python manage.py makemigrations" and executed, mainly to the database schema when running the command "python manage.py migrate")
    - **templates/**
        - **clock-in.html** (I created this to allow users to clock in)
        - **clock-out.html** (I created this to allow users to clock out, manually)
        - **history.html** (I created this to allow users to review their timesheet history, only allowing them to view their own history - my plan for the future is to associate a user with a team, where the team lead will be able to see all of the team members timesheets to generate statistics for their team as a whole)
    - **init.py** (This file helps register that this directory is a Python package/module)
    - **admin.py** (This file is auto-created when a Django app is initialized, and the information inside allows the admin side to register certain models, for instance, this file helps to register the Timesheet model)
    - **apps.py** (This file helps configure this directory/folder (core) as a Django app)
    - **models.py** (This file help structure the database for this project each model is a representation of the database schema - this one shows how I structured the Timesheet data)
    - **tests.py** (This file was automatically generated when I established the core app and is used to test the code throughout this app; however, I did not edit this file)
    - **views.py** (This file helps handle web requests (i.e. redirect, etc.), this holds the views for the clock in and clock out functionality, utilizing the login_required decorator user authentication in order to access these functions)
- **venv/** (This folder holds all of the information that is realtive to my environmental variables)
- **webapp_django/**
    - **pycache/** (This folder was automatically generated when I created the core app, I did not touch this folder and the files within)
    - **init.py** (This file tells Django to treat the webapp_django directory as a package)
    - **asgi.py** (This file helps run the Django server asynchronously, allowing the user to run the application while other processes run in the background)
    - **settings.py** (This file is the hub where settings are held (i.e. global variables, configure database connections and template locations))
    - **urls.py** (This is where all of the URL file paths are identified, I have inserted all paths, except 'admin/' - that was automatically generated when I initialized this project as a Django application)
    - **wsgi.py** (This file mimics asgi.py, but using a different interfacte to run the Django server)
- **.gitignore** (This file helps when the application is in production, as it contains language to exclude sensitive/secret environmental variables, database information, etc.  During my research on creating a Django application, it was suggested to copy from gitignore/Python.gitignore, since it is an open-source repository)
- **db.sqlite3** (This is the database file)
- **manage.py** (This file helps with administrative tasks (i.e. runserver and database migrations))
- **README.md** (documentation regarding the overview of this project)
- **requirements.txt** (This file holds a list of all relative packages or libraries needed to work on this project, I utilized the "pip freeze requirements.txt" command to document information to this file)


### Notes About My Process:

When determining what I should create as my final project, I gravitated towards Python (since it was a language that I picked up fairly easily).  I ended up taking a Python course through Udemy (titled The Complete Python Bootcamp From Zero to Hero by Jose Portilla) to further develop my Python skills.

I also watched the CS50 Seminars, from Week 10 and was interested in learning more about version control through Git.  I took another course in Udemy (titled The Git & Github Bootcamp by Colt Steele) to fully understand and use Git and Github.

After much thought of what to actually do for my final project, I thought of creating a timesheet that logged a user's location, in order to solve a problem that I encountered as an undergraduate at the University of California, Riverside.  I was a student worker in the library, and the timesheet that they used was not efficient - it would allow me to clock in anywhere, even when I wasn't physically at my work location.  My thought was to enable some sort of location services that documented where an employee clocked in and clocked out, in order for my employer to see if the employee was legitmately documenting time at their work location.

I re-watched the CS50 Flask lecture from Week 9.  I understood the Flask web framework, but wanted to explore Django.  I ended up going through many, many videos on youtube to digest the overall concept of Django, and saw many built-in functionalities that I imagined would apply to my web application (i.e. user authentication, ability to work with different databases).  One video that I found incredibly useful was: https://www.youtube.com/watch?v=fOukA4Qh9QA&t=3329s.  I ended up re-watching this video many times when applying features to my web application.  In this video, I came across Tailwind CSS and liked the fact that the CSS capabilities were written into the html (not a separate CSS file) through the use of classes.  I LOVED this about Tailwind CSS, because I find that writing CSS files are very tedious and I do not enjoy working with them.  I considered using Bootstrap, since that is what we learned in class, but I found it time consuming, and in order to generate a web application in a timely fashion, I used Tailwind CSS (mainly pre-built Tailwind components through Tailblocks https://tailblocks.cc/).

I plan on continuing to explore the capabilities of this web application using other functionalities of Python, Django, Tailwind CSS, etc.  One thing that I plan on researching is Geolocation services (i.e. Google Maps) and how to implement live-location tracking by displaying a map on the clock-in and clock-out html files.  This project has been instrumental to my learning (and self-confidence) of Python programming.