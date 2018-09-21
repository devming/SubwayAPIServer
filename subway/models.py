# coding: utf-8
from django.db import models
from .compose_subway_stations import shortest_path


# Create your models here.
class Admins(models.Model):
    admin_id = models.CharField(max_length=20)
    admin_pw = models.CharField(max_length=20)
    station = models.ForeignKey('Subway', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.admin_id


class Subway(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=50)
    line = models.CharField(max_length=20)
    fr_code = models.CharField(max_length=10)
    eng_name = models.CharField(max_length=50, null=True)
    landmarks = models.ForeignKey('SubwayLandmarkPoint', on_delete=models.CASCADE, null=True)
    up_station = models.CharField(max_length=20, default="", null=True)
    down_station = models.CharField(max_length=20, default="", null=True)

    def insert_stations(self, data, line, s):
        station = data[line][s]
        self.code = station["STATION_CD"]
        self.name = station["STATION_NM"]
        self.line = station["LINE_NUM"]
        self.fr_code = station["FR_CODE"]
        self.eng_name = station["STATION_NM_ENG"]
        if s > 0:
            self.up_station = data[line][s-1]["STATION_NM"]
        if s < len(data[line])-1:
            self.down_station = data[line][s+1]["STATION_NM"]
        self.save()

    def getShortestPath(self):
        stations = shortest_path()

    class Meta:
        ordering = ("fr_code", )


class SubwayLandmarkPoint(models.Model):
    station = models.ForeignKey(Subway, null=True, on_delete=models.CASCADE)
    station_name = models.CharField(max_length=20, null=False, default="Station Not Set")
    name = models.CharField(max_length=50, null=False, default="Landmark Not Set")
    # x = models.IntegerField
    # y = models.IntegerField
    # z = models.IntegerField
    left = models.CharField(max_length=20, null=False, default="")      # 하행선 (내선)
    right = models.CharField(max_length=20, null=False, default="")     # 상행선 (외선)
    qr_file_name = models.CharField(max_length=50, null=False, default="")
    url = models.CharField(max_length=100, null=False, default="")


# class History(models.Model):
#     source_point = models.ManyToOneRel(SubwayLandmarkPoint)
#     destination_point = models.ManyToOneRel(SubwayLandmarkPoint)
#     source_station = models.ManyToOneRel(Subway)
#     destination_station = models.ManyToOneRel(Subway)
