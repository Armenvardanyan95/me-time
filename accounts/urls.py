# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'get-auth-token/', views.GetAuthToken.as_view(), name='get-auth-token'),
    # url(r'forgot-password/', views.ForgotPasswordAPIView.as_view(), name='forgot-password'),
    # url(r'change-password/(?P<token>\w+)/$', views.ChangePasswordAPIView.as_view(), name='change-password'),
]
