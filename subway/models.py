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
    name = models.CharField(max_length=20)
    line = models.CharField(max_length=20)
    fr_code = models.CharField(max_length=10)
    landmarks = models.ForeignKey('SubwayLandmarkPoint', on_delete=models.CASCADE, null=True)
    up_station = models.CharField(max_length=20, default="", null=True)
    down_station = models.CharField(max_length=20, default="", null=True)

    def insert_stations(self, data, line, s):
        station = data[line][s]
        self.code = station["STATION_CD"]
        self.name = station["STATION_NM"]
        self.line = station["LINE_NUM"]
        self.fr_code = station["FR_CODE"]
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
    index = models.IntegerField
    station = models.ForeignKey(Subway, on_delete=models.CASCADE)
    # x = models.IntegerField
    # y = models.IntegerField
    # z = models.IntegerField
    left = models.CharField(max_length=5, null=False, default="")      # 0 = 하행선 (내선)
    right = models.CharField(max_length=5, null=False, default="")     # 1 = 상행선 (외선)

    def save_data(self, index, station, left, right):
        self.index = index
        self.station = station
        self.left = left
        self.right = right


# class History(models.Model):
#     source_point = models.ManyToOneRel(SubwayLandmarkPoint)
#     destination_point = models.ManyToOneRel(SubwayLandmarkPoint)
#     source_station = models.ManyToOneRel(Subway)
#     destination_station = models.ManyToOneRel(Subway)
