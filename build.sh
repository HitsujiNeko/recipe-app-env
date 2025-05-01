#!/usr/bin/env bash
set -e

cd RecipeSuggestion_project
python manage.py collectstatic --noinput
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py loaddata data.json
python manage.py superuser