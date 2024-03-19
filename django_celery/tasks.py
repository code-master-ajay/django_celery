from celery import shared_task
from time import sleep
import logging


log = logging.getLogger('my_app')


@shared_task
def my_task(x,y):
    sleep(5)

    # log.info(f"Task {my_task.request.id} is running")
    log.info(f"Task result is:{x+y}")
    return x+y