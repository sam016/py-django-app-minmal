import json
from ola.models import Customer, Ride
from api.serializers import CustomerSerializer, BookRideSerializer, CustomerListRideStatsSerializer
from django.db import connection
from django.http import HttpResponse
from django.forms.models import model_to_dict
from rest_framework import routers, serializers, viewsets, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


class CustomerList(generics.ListCreateAPIView):
    '''
    Provides a get/post method handler.
    '''
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Provides a get/put/delete method handler.
    '''
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    http_method_names = ['get', 'put', 'delete']


class CustomerRequestRide(APIView):
    '''
    Sends a request for a ride
    '''
    queryset = Customer.objects.all()
    serializer_class = BookRideSerializer
    http_method_names = ['post']


class CustomerListRideStats(generics.ListAPIView):
    serializer_class = CustomerListRideStatsSerializer

    def dictfetchall(self, cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

    def get_queryset(self):
        query = """
                SELECT
                    t.id,
                    t.username,
                    t.rides_count,
                    t.rides_requested,
                    t.rides_ongoing,
                    t.rides_completed,
                    t.last_updated_at
                FROM
                    (SELECT
                        c.id,
                        c.username,
                        COUNT(r.id) as rides_count,
                        SUM(CASE WHEN r.status=0 THEN 1 ELSE 0 END) as rides_requested,
                        SUM(CASE WHEN r.status=1 THEN 1 ELSE 0 END) as rides_ongoing,
                        SUM(CASE WHEN r.status=2 THEN 1 ELSE 0 END) as rides_completed,
                        MAX(r.updated_at) as last_updated_at
                    FROM ride as r
                    JOIN customer as c
                        ON c.id = r.customer_id
                    GROUP BY r.customer_id
                    ORDER BY last_updated_at DESC) as t
                """

        result = []

        with connection.cursor() as c:
            c.execute(query)
            result = self.dictfetchall(c)

        return result

    def list(self, request):
        result = self.get_queryset()

        return HttpResponse(json.dumps(result), content_type="application/json")
