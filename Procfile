release: python manage.py makemigrations --noinput
release: python manage.py migrate --noinput

web: gunicorn --chdir Lizania_api Lizania_api.wsgi