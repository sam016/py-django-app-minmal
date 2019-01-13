"""
Urls for the Ola App
"""
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
# from django.contrib import admin

# admin.autodiscover()


schema_view = get_schema_view(
   openapi.Info(
      title="Demo Ola Auto Q API",
      default_version='v1',
      description="This is an API implementaion describing the use of Ola Auto Q System",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="devmaster@sam016.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name='blog')
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path('', include('ola.urls')),
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    # path('admin/', admin.site.urls),

    re_path('swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
