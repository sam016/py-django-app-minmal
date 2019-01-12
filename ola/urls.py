"""
Coniguring the URLs at the app level
"""
from django.urls import path
from ola.views import index as v_index
from ola.views import driver as v_driver
from ola.views import customer as v_customer
from ola.views import dashboard as v_dashboard

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name='blog')
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path('', v_index.index, name='index'),
    path('customers/', v_customer.get_list, name='customer'),
    path('customers/<int:id>', v_customer.get_by_id, name='customer-id'),
    path('drivers/', v_driver.get_list, name='driver'),
    path('drivers/<int:id>', v_driver.get_by_id, name='driver-id'),
    path('dashboard/', v_dashboard.index, name='dashboard'),
]
