# python-pillow-qrcode
# qr "Do re mi faso" > doremi.png
import qrcode
import os

FILE = os.path.dirname(os.path.abspath(__file__))

img = qrcode.make('do re mi fasol')

print(type(img))
print(img.size)

img.save(FILE + "doremi.png")

qr = qrcode.QRCode()
qr.add_data('mas más mas')
qr.make()

img = qr.make_image()
img.save(FILE + 'test2.png')

qr = qrcode.QRCode(
    version=33,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=2,
    border=8
)
qr.add_data('mas más mas mas')
qr.make()

img = qr.make_image(fill_color="red", back_color='#469a19')
img.save(FILE + 'test_4.png')
