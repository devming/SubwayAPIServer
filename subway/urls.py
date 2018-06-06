from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.shortest_path, name='shortest_path'),
]
# https://www.sitepoint.com/building-simple-rest-api-mobile-applications/