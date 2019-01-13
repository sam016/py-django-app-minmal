from django.db import models
from django.utils import timezone
from .base import BaseModel

class Customer(BaseModel):
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return 'customer[{0}]: {1}'.format(self.id, self.username)

    def __unicode__(self):
        return 'customer[{0}]: {1}'.format(self.id, self.username)

    class Meta:
        db_table = 'customer'
        verbose_name_plural = 'Customers'
