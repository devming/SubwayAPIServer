from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^register_page$', views.register_landmark, name='register_page'),
    url(r'^admin_setting$', views.admin_setting, name='admin_setting'),
    url(r'^qr/(?P<station_admin_id>[-\w]+)/(?P<idx>\d+)/(?P<destination>[-\w]+)/$', views.return_qr, name='return_qr'),
]
# https://www.sitepoint.com/building-simple-rest-api-mobile-applications/