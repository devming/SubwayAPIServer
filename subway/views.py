#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

from subway.shortest_path import get_shortest_path
from .qrcode_generator import qrcode_generator
from .forms import LandmarkForm
from .forms import LoginForm
from .compose_subway_stations import shortest_path
from .models import Subway, Admins, SubwayLandmarkPoint
from subway.apikey import base_url


def dashboard(request):
    try:
        admin_info = Admins.objects.get(admin_id=request.session["admin_id"])
    except:
        return render(request, 'subway/dashboard.html')

    landmark_point_info = list(SubwayLandmarkPoint.objects.filter(station_name=admin_info.station.name))

    list_cnt = len(landmark_point_info)

    if list_cnt == 0:
        return render(request, 'subway/dashboard.html', {'admin': admin_info,
                                                         'empty_string': '등록된 Landmark Point가 없습니다.'})
    else:
        return render(request, 'subway/dashboard.html', {'admin': admin_info,
                                                         'landmark_point_info': landmark_point_info})


def register_landmark(request):
    try:
        admin_info = Admins.objects.get(admin_id=request.session["admin_id"])
    except:
        return render(request, 'subway/register_page.html')
    # landmark_count = len(list(SubwayLandmarkPoint.objects.filter(station_name=admin_info.station.name)))
    try:
        landmark_index = str(int(len(list(SubwayLandmarkPoint.objects.all()))) + 1)
    except IndexError:
        landmark_index = "0"

    if request.method == "POST":
        form = LandmarkForm(request.POST)
        name = request.POST.get('landmark_name')
        left_station = request.POST.get('left').split('-')[0]
        right_station = request.POST.get('left').split('-')[1]

        if form.is_valid():
            form.station = admin_info.station
            form.station_name = admin_info.station.name
            form.landmark_name = name
            form.left = left_station
            form.right = right_station
            qr_image_name = qrcode_generator(admin_info.admin_id, landmark_index)
            url = base_url+"qr/"+admin_info.admin_id+"/"+landmark_index
            subway_landmark = SubwayLandmarkPoint(station=form.station, station_name=form.station_name,
                                                  name=form.landmark_name, left=form.left, right=form.right,
                                                  qr_file_name=qr_image_name, url=url)
            subway_landmark.save()
            return redirect('/')
    else:
        form = LandmarkForm()

    return render(request, 'subway/register_page.html', {'form': form,
                                                         'station': admin_info.station,
                                                         'admin': admin_info,
                                                         'landmark_cnt': landmark_index,
                                                         'up_station': Subway.objects.get(name=admin_info.station.name).up_station,
                                                         'down_station': Subway.objects.get(name=admin_info.station.name).down_station})


# 앱에서 QR코드를 찍으면 idx까지의 url을 string으로 전달 받고,
# 뒤에 /{destination역이름}을 붙여서 다시 return_qr로 전송하게 된다.
def return_qr(request, station_admin_id, idx, destination):
    station = Admins.objects.get(admin_id=station_admin_id).station
    landmark = SubwayLandmarkPoint.objects.get(id=idx, station_name=station.name)
    left = landmark.left
    right = landmark.right

    print("## 1 ##")
    print(destination)
    # TODO: shortest path 에서 다음 역이 left이면 1 right이면 2, 잘못된 값이면 0 반환
    response_left_parameter = get_shortest_path(station.name, destination, left, right)

    data = {}
    data['stationName'] = station.name
    data['direction'] = response_left_parameter

    print(data)

    return HttpResponse(json.dumps(data), content_type=u"application/json; charset=utf-8")


def admin_setting(request):
    try:
        admin_info = Admins.objects.get(admin_id=request.session["admin_id"])
    except:
        return render(request, 'subway/admin_setting.html')
    name = Subway.objects.get(name=admin_info.station.name).name
    return render(request, 'subway/admin_setting.html', {'admin': admin_info, 'station_name': name})


def login(request):
    if request.method == "POST":
        # form = LoginForm(request.POST)
        admin_id = request.POST['admin_id']
        admin_pw = request.POST['admin_pw']
        try:
            login = Admins.objects.get(admin_id=admin_id)
        except:
            return render(request, 'subway/dashboard.html')

        if login.admin_pw == admin_pw:
            request.session['admin_id'] = login.admin_id
            print("Login Success")
        else:
            print("Login Fail")
            return render(request, 'subway/dashboard.html')
    else:
        form = LoginForm()

    try:
        admin_info = Admins.objects.get(admin_id=admin_id)
    except:
        print("Login ERROR")
        return render(request, 'subway/dashboard.html')

    landmark_point_info = list(SubwayLandmarkPoint.objects.filter(station_name=admin_info.station.name))

    list_cnt = len(landmark_point_info)

    if list_cnt == 0:
        return render(request, 'subway/dashboard.html', {'admin': admin_info,
                                                         'empty_string': '등록된 Landmark Point가 없습니다.'})
    else:
        return render(request, 'subway/dashboard.html', {'admin': admin_info,
                                                         'landmark_point_info': landmark_point_info})


def logout(request):
    try:
        del request.session['admin_id']
    except KeyError:
        pass
    return render(request, 'subway/dashboard.html')

# 한 번만 호출
def insert_station_datas(request):
    data = shortest_path()

    for line in data:
        for station in range(len(data[line])):
            Subway().insert_stations(data, line, station)
    return redirect('/')

# https://github.com/cyrus-and/gdb-dashboard/issues/61 - 인코딩 에러 해결 방법
# export LC_ALL=C.UTF-8