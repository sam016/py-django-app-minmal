from django.db import models
from django.utils import timezone
from .base import BaseModel


class Ride(BaseModel):
    customer = models.ForeignKey(
        'Customer', related_name='customer', on_delete=models.CASCADE)
    driver = models.ForeignKey(
        'Driver', related_name='driver', on_delete=models.CASCADE)
    requested_at = models.DateTimeField(editable=False)
    started_at = models.DateTimeField(null=True)
    finished_at = models.DateTimeField(null=True)

    def __unicode__(self):
        return 'ride[{0}]: {1}'.format(self.id, self.name)

    class Meta:
        db_table = 'ride'
        verbose_name_plural = 'Rides'
