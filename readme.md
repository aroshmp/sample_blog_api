Rest Framework Installation
==============================
pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter

We need to add a few things to our settings.py file.
INSTALLED_APPS = [
    ...
    'rest_framework',
]