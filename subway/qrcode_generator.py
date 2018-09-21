# coding: utf-8
import qrcode


# url = http://ec2-13-125-207-134.ap-northeast-2.compute.amazonaws.com/qr/{admin_id}/{landmark_index}
# file_name = {admin_id}_{landmark_index}.png
from server.settings import STATIC_URL
from subway.apikey import base_url


def qrcode_generator(admin_id, landmark_index):
    url = base_url+"qr/"+admin_id+"/"+landmark_index
    file_full_path_name = "myproject/subway"+STATIC_URL+"qrs/"+admin_id+"_"+landmark_index+".png"
    file_name = admin_id + "_" + landmark_index + ".png"

    print("url: " + url)
    print("file_full_path_name: " + file_full_path_name)
    img = qrcode.make(url)
    print("++++++++++++++++++++")
    img.save(file_full_path_name, "PNG")
    print("====================")
    return file_name
