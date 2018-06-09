from django.shortcuts import render, redirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from subway.compose_subway_stations import shortest_path
from subway.models import Subway, Admins, SubwayLandmarkPoint


# def get_rest_list(request):
#     """
#     List all restaurants
#     """
#     rest_list = Subway.objects.order_by('-fr_code')
#     serializer = RestaurantSerializer(rest_list, many=True)
#     return JsonResponse(serializer.data, safe=False)

# Rest framework
# @csrf_exempt
# def station_admin(request):
#     return JsonResponse()

def dashboard(request):

    admin_info = Admins.objects.get(admin_id='skku')
    landmark_point_info = SubwayLandmarkPoint.objects.filter(station__name='성균관대')
    # landmark_point_info = SubwayLandmarkPoint.objects.all().name

    return render(request, 'subway/dashboard.html', {'station': admin_info.station, 'landmark_point': landmark_point_info})


def register_landmark(request):

    admin_info = Admins.objects.get(admin_id='skku')

    if Subway.objects.get(name=admin_info.station.name).landmarks is None:
        landmark_count = 0
    else:
        landmark_count = len(list(Subway.objects.get(name=admin_info.station.name).landmarks))
    return render(request, 'subway/register_page.html', {'station': admin_info.station,
                                                      'admin': admin_info,
                                                      'landmark_cnt': landmark_count})
    # return render('subway/register_page.html', RequestContext(request, {'station': admin_info.station,
    #                                                   'admin': admin_info,
    #                                                   'landmark_cnt': landmark_count}))


def admin_setting(request):
    subway_station_json = shortest_path()
    return render(request, 'subway/admin_setting.html', {'stations': subway_station_json})


def register_landmark_point(request):
    name = request.station_name
    index = request.index
    direction = request.direction

    station = Subway.objects.get(name=name)
    # station[0].name
    SubwayLandmarkPoint().save_data(index+1, station, '의왕', '화서')

    landmark = SubwayLandmarkPoint.objects.get(station=station)
    return redirect(request, 'subway/dashboard.html', {'landmark': landmark})



# 한 번만 호출
def insert_station_datas():
    data = shortest_path()

    for line in data:
        for station in range(len(data[line])):
            Subway().insert_stations(data, line, station)