release: cd api && python manage.py migrate
web: gunicorn --chdir ./api api.wsgi --log-file -