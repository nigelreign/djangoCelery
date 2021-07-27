"""
    @author Nigel Zulu
    Email zulunigelb@gmail.com
    Created on 29/6/2021
"""

import json


from django.core.mail.message import EmailMultiAlternatives, BadHeaderError
from celery.decorators import task
from celery import shared_task
from celery.utils.log import get_task_logger

from datetime import datetime

logger = get_task_logger(__name__)

@task(name="send_email")
def send_email(email_address):

    logger.info("I have sent the email to"+ email_address)
