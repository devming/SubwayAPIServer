import qrcode


# url = http://ec2-13-125-207-134.ap-northeast-2.compute.amazonaws.com/qr/{admin_id}/{landmark_index}
# file_name = {admin_id}_{landmark_index}.png
from server.settings import STATIC_URL


def qrcode_generator(admin_id, landmark_index):
    url = "http://ec2-13-125-207-134.ap-northeast-2.compute.amazonaws.com:8000/qr/"+admin_id+"/"+landmark_index
    file_full_path_name = "subway"+STATIC_URL+"qrs/"+admin_id+"_"+landmark_index+".jpg"
    file_name = admin_id + "_" + landmark_index + ".jpg"
    # qr = qrcode.QRCode(
    #     version=1,
    #     error_correction=qrcode.constants.ERROR_CORRECT_L,
    #     box_size=10,
    #     border=4,
    # )
    # qr.make(fit=True)
    # img = qr.make_image(fill_color="black", back_color="white")
    #
    # print(type(img))
    # return img

    img = qrcode.make(url)
    img.save(file_full_path_name)
    return file_name