from ola.models import Driver
from rest_framework import routers, serializers, viewsets, generics

# Serializers define the API representation.


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ('id', 'username', 'first_name', 'last_name',
                  'ongoing_rides_count', 'finished_rides_count', 'updated_at', 'created_at')
