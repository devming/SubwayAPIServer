from django.db import models
from .compose_subway_stations import shortest_path


# Create your models here.
class Administrators(models.Model):
    admin_id = models.CharField(max_length=20)
    admin_pw = models.CharField(max_length=20)
    station = models.ForeignKey('Subway', on_delete=models.CASCADE, null=True)


class Subway(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=20)
    line = models.CharField(max_length=20)
    fr_code = models.CharField(max_length=10)
    landmarks = models.ForeignKey('SubwayLandmarkPoint', on_delete=models.CASCADE, null=True)

    def insert_stations(self):
        stations = shortest_path()

    class Meta:
        ordering = ("fr_code", )


class SubwayLandmarkPoint(models.Model):
    landmark_index = models.IntegerField
    station = models.ForeignKey(Subway, on_delete=models.CASCADE)
    x = models.IntegerField
    y = models.IntegerField
    z = models.IntegerField
    left = models.BooleanField      # 0 = 하행선 (내선)
    right = models.BooleanField     # 1 = 상행선 (외선)


# class History(models.Model):
#     source_point = models.ManyToOneRel(SubwayLandmarkPoint)
#     destination_point = models.ManyToOneRel(SubwayLandmarkPoint)
#     source_station = models.ManyToOneRel(Subway)
#     destination_station = models.ManyToOneRel(Subway)
