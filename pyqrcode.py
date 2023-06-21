import qrcode
s = input("Please enter url: ")
qr_img = qrcode.make(s)
qr_img.save("qr-img.jpg")
