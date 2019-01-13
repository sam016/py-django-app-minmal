import datetime
import humanize
from django.db import models
from django.utils import timezone
from .base import BaseModel


class Ride(BaseModel):
    RIDER_WAITING = 0
    RIDER_ONGOING = 1
    RIDER_COMPLETE = 2
    RIDER_STATUS = (
        (RIDER_WAITING, 'Waiting'),
        (RIDER_ONGOING, 'Ongoing'),
        (RIDER_COMPLETE, 'Complete'), )

    customer = models.ForeignKey(
        'Customer', related_name='customer', on_delete=models.CASCADE)
    driver = models.ForeignKey(
        'Driver', related_name='driver', on_delete=models.CASCADE, null=True)
    requested_at = models.DateTimeField(editable=False, auto_now_add=True)
    started_at = models.DateTimeField(null=True)
    finished_at = models.DateTimeField(null=True)
    status = models.SmallIntegerField(
        choices=RIDER_STATUS,
        default=RIDER_WAITING, )

    @property
    def customer_username(self):
        return self.customer.username

    @property
    def driver_username(self):
        return self.driver.username if self.driver else None

    @property
    def time_elapsed(self):
        if self.finished_at:
            return humanize.naturaltime(datetime.datetime.utcnow() - self.finished_at.replace(tzinfo=None))

        if self.started_at:
            return humanize.naturaltime(datetime.datetime.utcnow() - self.started_at.replace(tzinfo=None))

        return humanize.naturaltime(datetime.datetime.utcnow() - self.requested_at.replace(tzinfo=None))

    def __unicode__(self):
        return 'ride[{0}]: {1}'.format(self.id, self.name)

    class Meta:
        db_table = 'ride'
        verbose_name_plural = 'Rides'
