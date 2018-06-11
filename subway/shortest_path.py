import json
import requests as req

NONE = 0
LEFT = 1
RIGHT = 2
SEARCH_BASE = "http://swopenapi.seoul.go.kr/api/subway/"


def api_shortest_path(api_key, text_format, api_name, start_page, end_pPage, start_station, end_station):
    url = SEARCH_BASE + api_key + '/' + text_format + '/' + api_name + '/' + start_page
    url = url + '/' + end_pPage + '/' + start_station + '/' + end_station
    r = req.get(url)
    json_data = json.loads(r.text)
    print("\njsonData:"+r.text)
    return json_data


def get_shortest_path(start_station, end_station, left_station, right_station):
    # Load API Key
    f = open('./.apikey', 'r')
    api_key = str(f.read())[:-1]
    f.close()

    json_data_path = api_shortest_path(api_key, 'json', 'shortestRoute', '1', '1', start_station, end_station)

    station_name_list = json_data_path['shortestRouteList'][0]['shtStatnNm'].split(',')
    travel_msg = json_data_path['shortestRouteList'][0]['minTravelMsg']

    for s in station_name_list:
        print("station_name_list: " + s)
    # startLineNumber example => 1002, 1004, 1007 ... 100line number
    start_line_number = json_data_path['shortestRouteList'][0]['shtStatnId'].split(',')[0][:4]
    print("\nCurrent Station(station_name_list[0]) : " + station_name_list[0])
    print("Next Station(station_name_list[1]) : " + station_name_list[1])
    print("Travel Msg(travel_msg) : " + travel_msg)

    if right_station == station_name_list[1]:
        return RIGHT
    elif left_station == station_name_list[1]:
        return LEFT
    else:
        return NONE
