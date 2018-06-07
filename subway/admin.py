from django.contrib import admin

# Register your models here.
from .models import Subway, SubwayLandmarkPoint, Admins

admin.site.register(Admins)
admin.site.register(Subway)
admin.site.register(SubwayLandmarkPoint)
