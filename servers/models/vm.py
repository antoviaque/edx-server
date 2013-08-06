
# Imports ###########################################################

from django.db import models

from common import TimeStampedModel
from server import Server


# Choices ###########################################################

VM_STATUS_CHOICES = (
    ('creating', 'VM is being created'),
    ('created', 'VM has been created'),
    ('deleting', 'VM is being deleted'),
    ('deleted', 'VM has been deleted'),
)


# Classes ###########################################################

class VM(TimeStampedModel):
    server = models.ForeignKey(Server)
    os_id = models.CharField(max_length=200)
    status = models.CharField(default='creating', choices=VM_STATUS_CHOICES, max_length=10)

    class Meta:
            app_label = 'servers'
    
    def __unicode__(self):
        return u'<VM: {0} ({1})>'.format(self.os_id, self.status)
