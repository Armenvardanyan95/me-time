from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class AbstractBaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):

        self.modified = timezone.now()
        return super(AbstractBaseModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True
