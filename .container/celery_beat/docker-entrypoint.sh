#!/usr/bin/env bash
set -e
shopt -s extglob globstar

# Activate venv
source $VENV_HOME/bin/activate
cd $SRC_HOME
celery beat -A celery_app.celery --loglevel=$LOG_LEVEL --scheduler django_celery_beat.schedulers:DatabaseScheduler
