from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^register_page', views.register_landmark, name='register_landmark'),
    url(r'^admin_setting$', views.admin_setting, name='admin_setting'),
    url(r'^register_landmark_point', views.register_landmark_point, name='register_landmark_point'),

]
# https://www.sitepoint.com/building-simple-rest-api-mobile-applications/