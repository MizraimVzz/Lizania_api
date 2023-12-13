release: python manage.py makemigrations --noinput
release: python manage.py migrate --noinput

web: gunicorn Lizania_api.wsgi