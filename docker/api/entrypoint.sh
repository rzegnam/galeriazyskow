#!/bin/sh
cd /code/galeria
scrapy crawl prawie
cd /code/rest
python manage.py makemigrations
python manage.py migrate
exec "$@"
