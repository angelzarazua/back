from django.conf.urls import url
from Gps.views import *

urlpatterns = [
    url(r'^createGps/', GpsList.as_view(), name='GPS')
]