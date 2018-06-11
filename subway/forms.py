from django import forms

from .models import SubwayLandmarkPoint
from .models import Subway
from .models import Admins


class LandmarkForm(forms.Form):

    # st_admin_info = Admins.objects.get(admin_id='skku').station
    # up = st_admin_info.up_station
    # down = st_admin_info.down_station
    #
    # CHOICES = (('1', up+"-"+down), ('2', down+"-"+up))

    station = forms.CharField(required=False)
    station_name = forms.CharField(required=False)
    landmark_name = forms.CharField(required=False)
    left = forms.CharField(widget=forms.RadioSelect, required=False)
    right = forms.CharField(widget=forms.RadioSelect, required=False)



    # def get_readonly(self):
    #     self.station.widget.attrs['readonly'] = "readonly"

    # class Meta:
    #     model = SubwayLandmarkPoint
    #     fields = ('station', 'left', 'right',)
