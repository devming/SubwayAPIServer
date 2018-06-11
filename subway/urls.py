from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^register_page$', views.register_landmark, name='register_page'),
    url(r'^admin_setting$', views.admin_setting, name='admin_setting'),
    # url(r'^qr/(?P<slug>[-\w]+)/^(?P<pk>\d+)/$', views.return_qr, name='return_qr'),
    url(r'^qr/(?P<station_admin_id>[-\w]+)/(?P<idx>\d+)/$', views.return_qr, name='return_qr'),
    # url(r'^register_landmark_point$', views.register_landmark_point, name='register_landmark_point'),
    # url(r'^qr/^[a-zA-Z]*/^[0-9]*$', views.return_qr, name='return_qr'),
]
# https://www.sitepoint.com/building-simple-rest-api-mobile-applications/