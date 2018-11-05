release find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
release find . -path "*/migrations/*.pyc"  -delete
release python3 ./SGEHookah/manage.py makemigrations --noinput
release python3 ./SGEHookah/manage.py migrate
release python3 ./SGEHookah/manage.py initadmin
web: gunicorn SGEHookah.wsgi
