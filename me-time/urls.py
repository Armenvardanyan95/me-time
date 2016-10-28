from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^' + settings.API_VERSION_URL, include(router.urls, namespace='api')),
]
