import logging

from celery.utils.log import get_task_logger

from celery_app.celery import app

logger = get_task_logger(__name__)


@app.task(bind=True, name='celery_app.task.test_scheduling_tasks')
def task_test_scheduling_tasks():
    task_name = '[test_scheduling_tasks]'
    message = '{task_name} Running scheduling task for tests'.format(task_name=task_name)
    logging.info(message)
    logger.info(message)
