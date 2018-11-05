release find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
release find . -path "*/migrations/*.pyc"  -delete
release python manage.py makemigrations --noinput
release python manage.py migrate
release python manage.py initadmin
web: gunicorn SGEHookah.wsgi
