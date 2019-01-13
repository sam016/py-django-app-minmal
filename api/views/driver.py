from ola.models import Driver
from api.serializers import DriverSerializer
from rest_framework import routers, serializers, viewsets, generics


class DriverList(generics.ListCreateAPIView):
    '''
    Provides a get method handler.
    '''
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class DriverDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Provides a get method handler.
    '''
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    http_method_names = ['get', 'put', 'delete']
