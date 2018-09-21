# coding: utf-8
from django import forms

from .models import SubwayLandmarkPoint
from .models import Subway
from .models import Admins


class LandmarkForm(forms.Form):
    station = forms.CharField(required=False)
    station_name = forms.CharField(required=False)
    landmark_name = forms.CharField(required=False)
    left = forms.CharField(widget=forms.RadioSelect, required=False)
    right = forms.CharField(widget=forms.RadioSelect, required=False)


class LoginForm(forms.Form):
    admin_id = forms.CharField(required=False)
    admin_pw = forms.CharField(required=False)
