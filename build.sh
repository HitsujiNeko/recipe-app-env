#!/usr/bin/env bash
set -e

cd RecipeSuggestion_project
python manage.py collectstatic --noinput
python manage.py makemigrations --noinput
python manage.py migrate --noinput
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='takumid0419').exists() or User.objects.create_superuser('takumid0419', 'takumid0419@outlook.com', 'takumido200204')" | python manage.py shell