from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import ola.views
import ola.urls

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name='blog')
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path('', include('ola.urls')),
    path('admin/', admin.site.urls),
]