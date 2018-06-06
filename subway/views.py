from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from subway.compose_subway_stations import shortest_path
from subway.models import Subway


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


def station_admin(request):
    subway_station_json = shortest_path()
    subway_station_json["line1"]
    return render(request, 'subway/admin_main.html', {'stations': subway_station_json["line1"]})
