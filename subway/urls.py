from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.station_admin, name='station_admin'),
]
# https://www.sitepoint.com/building-simple-rest-api-mobile-applications/