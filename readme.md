# Full Stack Template

## Backend 

To start the backend:

```
cd backend/mysite
pipenv run python manage.py makemigrations && pipenv run python manage.py migrate
pipenv run python manage.py createsuperuser
pipenv run python manage.py runserver >>django.log 2>&1
```