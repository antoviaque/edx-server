
# Imports ###########################################################

from django.db import models
from django.utils.timezone import now


# Classes ###########################################################

class TimeStampedModel(models.Model):
    created_on = models.DateTimeField(null=True, default=now, db_index=True)
    updated_on = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.updated_on = now()
        super(TimeStampedModel, self).save(*args, **kwargs)

