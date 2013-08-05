
# Imports ###########################################################

from django.conf import settings
from django.db import models

from common import TimeStampedModel


# Choices ###########################################################

VM_STATUS_CHOICES = (
    ('creating', 'VM is being created'),
    ('created', 'VM has been created'),
    ('deleting', 'VM is being deleted'),
    ('deleted', 'VM has been deleted'),
)


# Classes ###########################################################

class Server(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=200)
    mysql_password = models.CharField(max_length=200)
    mongodb_password = models.CharField(max_length=200)

class VM(TimeStampedModel):
    server = models.ForeignKey(Server)
    os_id = models.CharField(max_length=200)
    status = models.CharField(default='creating', choices=VM_STATUS_CHOICES, max_length=10)

