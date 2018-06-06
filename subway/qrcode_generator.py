import qrcode


def qrcode_generator(url):
    img = qrcode.make(url)
    img.save("파일명.png")
    qrcode.clear()
    return img
