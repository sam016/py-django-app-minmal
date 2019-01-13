"""
Coniguring the URLs at the app level
"""
from django.urls import path
from .views import customer as v_customer
from .views import driver as v_driver
from .views import ride as v_ride

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name='blog')
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path('customers/', v_customer.CustomerList.as_view(), name='customers-list'),
    # path('customers/ride-stats/', v_customer.CustomerListRideStatsViewSet.as_view({'get': 'list'}) , name='customers-list-ride-stats'),
    path('customers/ride-stats/', v_customer.CustomerListRideStats.as_view(),
         name='customers-list-ride-stats'),
    path('customers/<int:pk>/',
         v_customer.CustomerDetail.as_view(), name='customer-id'),

    path('drivers/', v_driver.DriverList.as_view(), name='drivers-list'),
    path('drivers/<int:pk>/', v_driver.DriverDetail.as_view(), name='driver-id'),

    path('rides/', v_ride.RideList.as_view(), name='rides-list'),
    path('rides/book/', v_ride.BookRide.as_view(), name='ride-book'),
    path('rides/<int:pk>/', v_ride.RideDetail.as_view(), name='ride-id'),
    path('rides/<int:pk>/accept', v_ride.AcceptRide.as_view(), name='ride-accept'),
    path('rides/<int:pk>/finish', v_ride.FinishRide.as_view(), name='ride-finish'),
]
