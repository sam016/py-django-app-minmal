"""
Coniguring the URLs at the app level
"""
from django.urls import path
from ola.views import index as v_index
from ola.views import db as v_db

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name='blog')
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path('', v_index.index, name='index'),
    path('db/', v_db.index, name='db'),
]
