release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input

web: gunicorn --chdir Lizania_api Lizania_api.wsgi