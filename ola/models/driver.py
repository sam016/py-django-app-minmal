from django.db import models
from django.utils import timezone
from .base import BaseModel


class Driver(BaseModel):
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True)
    
    def __unicode__(self):
        return 'driver[{0}]: {1}'.format(self.id, self.name)

    class Meta:
        db_table = 'driver'
        verbose_name_plural = 'Drivers'
