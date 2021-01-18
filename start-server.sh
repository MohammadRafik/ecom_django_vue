#!/usr/bin/env bash
# start-server.sh

# if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
#     (python src/manage.py createsuperuser --no-input)
# fi

(cd src; gunicorn djangobase.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3) &
nginx -g "daemon off;"