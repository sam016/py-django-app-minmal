from django.db import models
from django.utils import timezone
from .base import BaseModel
from ola.models.ride import Ride


class Driver(BaseModel):
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True)

    @property
    def ongoing_rides_count(self):
        return Ride.objects.filter(driver__id=self.id, status=Ride.RIDER_ONGOING).count()

    @property
    def finished_rides_count(self):
        return Ride.objects.filter(driver__id=self.id, status=Ride.RIDER_COMPLETE).count()        

    def __str__(self):
        return 'customer[{0}]: {1}'.format(self.id, self.username)

    def __unicode__(self):
        return 'customer[{0}]: {1}'.format(self.id, self.username)

    class Meta:
        db_table = 'driver'
        verbose_name_plural = 'Drivers'
