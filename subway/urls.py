from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.register_landmark, name='station_admin'),
    url(r'^admin_setting', views.admin_setting, name='admin_setting'),
]
# https://www.sitepoint.com/building-simple-rest-api-mobile-applications/