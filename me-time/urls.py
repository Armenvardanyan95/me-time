from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from accounts.views import UsersViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UsersViewSet, base_name='users')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^' + settings.API_VERSION_URL, include(router.urls, namespace='api')),
    url(r'^' + settings.API_VERSION_URL + 'auth-users/', include('accounts.urls', namespace='auth-users'))
]
