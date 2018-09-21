
from subway import shortest_path
from subway.models import Subway


# 한 번만 호출
def insert_station_datas():
    data = shortest_path()

    for line in data:
        for station in range(len(data[line])):
            Subway().insert_stations(data, line, station)