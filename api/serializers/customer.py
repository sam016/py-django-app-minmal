from ola.models import Customer
from rest_framework import routers, serializers, viewsets, generics

# Serializers define the API representation.


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'username', 'first_name',
                  'last_name', 'updated_at', 'created_at')


class CustomerListRideStatsSerializer(serializers.ListSerializer):
    # id = serializers.IntegerField()
    # username = serializers.CharField(max_length=30)
    # rides_count = serializers.IntegerField()
    # rides_requested = serializers.IntegerField()
    # rides_ongoing = serializers.IntegerField()
    # rides_completed = serializers.IntegerField()
    # last_updated_at = serializers.DateTimeField()

    class Meta:
        fields = '__all__'
