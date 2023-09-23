#!/bin/bash

# Выполнение миграций и сборки статики
poetry install
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py test -v 2

# Запуск Gunicorn
exec "$@"
