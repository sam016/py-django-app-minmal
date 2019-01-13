from ola.models import Ride
from rest_framework import routers, serializers, viewsets, generics, filters

# Serializers define the API representation.


class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = ('id', 'customer', 'customer_username', 'driver', 'driver_username', 'status', 'requested_at',
                  'started_at', 'finished_at', 'time_elapsed', 'updated_at', 'created_at',)


class BookRideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = ('id', 'customer', 'driver', 'status', 'requested_at',
                  'started_at', 'finished_at', 'updated_at', 'created_at',)
        read_only_fields = ('id', 'driver', 'status', 'requested_at',
                            'started_at', 'finished_at', 'updated_at', 'created_at',)


class AcceptRideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = ('id', 'customer', 'driver', 'status', 'requested_at',
                  'started_at', 'finished_at', 'updated_at', 'created_at',)
        read_only_fields = ('id', 'customer', 'status', 'requested_at',
                            'started_at', 'finished_at', 'updated_at', 'created_at',)


class FinishRideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = ('id', 'customer', 'driver', 'status', 'requested_at',
                  'started_at', 'finished_at', 'updated_at', 'created_at',)
        read_only_fields = ('id', 'customer', 'driver', 'status', 'requested_at',
                            'started_at', 'finished_at', 'updated_at', 'created_at',)
