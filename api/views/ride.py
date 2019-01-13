from ola.models import Ride, Customer, Driver
from api.serializers import RideSerializer, BookRideSerializer, AcceptRideSerializer, FinishRideSerializer
from datetime import datetime
from django.db import transaction
from rest_framework import routers, serializers, viewsets, generics, filters
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView


class RideList(generics.ListAPIView):
    '''
    Provides a get method handler.
    '''
    queryset = Ride.objects.all()
    serializer_class = RideSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('username', 'status',
                       'requested_at', 'started_at', 'finished_at',)


class RideDetail(generics.RetrieveAPIView):
    '''
    Provides a get method handler.
    '''
    queryset = Ride.objects.all()
    serializer_class = RideSerializer


class BookRide(generics.CreateAPIView):
    '''
    Book a ride
    '''
    queryset = Ride.objects.all()
    serializer_class = BookRideSerializer

    def post(self, request, *args, **kwargs):
        customer = request.data.get('customer')
        if customer and isinstance(customer, str) and not customer.isdigit():
            cust_id = Customer.objects.filter(
                username=customer).values_list('id', flat=True).first()

            # if customer is not present by that username create one
            if not cust_id:
                customer = Customer(username=customer, first_name=customer)
                customer.save()
                cust_id = customer.id

            request.data['customer'] = cust_id

        return self.create(request, *args, **kwargs)


class BaseUpdateRideApiView(generics.UpdateAPIView):
    '''
    base Update Ride ApiView
    with validation and other userful methods
    '''
    http_method_names = ['put']
    lookup_url_kwarg = 'pk'

    def get_queryset(self):
        pk = self.kwargs.get(self.lookup_url_kwarg)
        rides = Ride.objects.filter(id=pk)
        return rides

    def get_ride(self):
        ride = self.get_queryset().first()
        if not ride:
            raise ValidationError('Ride does not exist')

        return ride


class AcceptRide(BaseUpdateRideApiView):
    '''
    Accept a ride
    '''
    serializer_class = AcceptRideSerializer

    def put(self, request, *args, **kwargs):
        driver = request.data.get('driver')
        if driver and isinstance(driver, str) and not driver.isdigit():
            drvr_id = Driver.objects.filter(
                username=driver).values_list('id', flat=True).first()

            # if driver is not present by that username create one
            if not drvr_id:
                driver = Driver(username=driver, first_name=driver)
                driver.save()
                drvr_id = driver.id

            request.data['driver'] = drvr_id

        with transaction.atomic():
            ride = self.get_ride()

            print(self.kwargs)

            if ride.driver:
                raise ValidationError('Ride is already picked up')

            ride.started_at = datetime.now()
            ride.status = Ride.RIDER_ONGOING
            ride.save()
            # kwargs['started_at'] = datetime.now()

            return self.update(request, *args, **kwargs)


class FinishRide(BaseUpdateRideApiView):
    '''
    Finish a ride
    '''
    serializer_class = FinishRideSerializer

    def put(self, request, *args, **kwargs):
        with transaction.atomic():
            ride = self.get_ride()

            if ride.finished_on:
                raise ValidationError('Ride is already finished')

            ride.finished_at = datetime.now()
            ride.status = Ride.RIDER_COMPLETE
            ride.save()
            # kwargs['finished_at'] = datetime.now()

            return self.update(request, *args, **kwargs)
