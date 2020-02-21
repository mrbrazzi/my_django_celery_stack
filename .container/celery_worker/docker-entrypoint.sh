#!/usr/bin/env bash
set -e
shopt -s extglob globstar

# Activate venv
source $VENV_HOME/bin/activate
cd $SRC_HOME
python manage.py migrate
celery worker -A celery_app.celery -E --loglevel=$LOG_LEVEL
