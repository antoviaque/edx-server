
# Imports ###########################################################

import logging

from celery.result import AsyncResult
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

from common import TimeStampedModel
from servers.tasks.openstack import nova_boot


# Globals ###########################################################

logger = logging.getLogger(__name__)


# Functions #########################################################

def make_random_password():
    User = get_user_model()
    return User.objects.make_random_password(length=20)


# Exceptions ########################################################

class OperationAlreadyInProgress(Exception):
    pass


# Classes ###########################################################

class ServerManager(models.Manager):
    
    def create_server(self, user):
        logger.info(u'Creating server for {user}', user=user)
        server, created = self.get_or_create(user=user, name=user.username)
        server.boot_vm()

        return server.pk


class Server(TimeStampedModel):
    """
    A logical instance of a whole edX portal (CMS, LMS & related services)
    Can be comprised of one or several VMs
    """
    objects = ServerManager()

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=200)
    mysql_password = models.CharField(max_length=200, default=make_random_password)
    mongodb_password = models.CharField(max_length=200, default=make_random_password)
    task_id = models.CharField(blank=True, max_length=36)
    
    class Meta:
        app_label = 'servers'

    def __unicode__(self):
        return u'<Server: {0}>'.format(self.name)
        
    def boot_vm(self):
        if self.task_id:
            raise OperationAlreadyInProgress

        vm_name = 'edx-single-{0}'.format(self.name)
        task = nova_boot.apply_async((vm_name, ))
        self.task_id = task.task_id
        self.save()

    def get_task(self):
        return self.task_id and AsyncResult(self.task_id)

    def get_task_result(self):
        task = self.get_task()
        if task is None:
            return u'No task'
        if not task.ready():
            return u'In progress...'
        return task.get()

    # TODO: Workflow:
    #   - Upon ended task, clean related server
    #   - Error handling when task fails
