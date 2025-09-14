check version : python -m django --version


## Create Django Project

django-admin startproject mysite
cd mysite
python manage.py runserver

project structure--

mysite/
│── manage.py        # command-line utility
│── mysite/          # project package
│   │── __init__.py
│   │── settings.py  # project settings
│   │── urls.py      # routing system
│   │── asgi.py
│   └── wsgi.py





open http://127.0.0.1:8000/in your browser → you’ll see Django’s welcome page 🎉





## Create your first app

python manage.py startapp hello

this create --

hello/
│── admin.py
│── apps.py
│── migrations/
│── models.py
│── tests.py
│── views.py
└── __init__.py


------------------------
## connect view to url
