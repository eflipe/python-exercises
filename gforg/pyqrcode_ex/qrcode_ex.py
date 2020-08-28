import pyqrcode
import png
from pyqrcode import QRCode

msj = "https://pbs.twimg.com/media/EghCeIRUcAAGkSO?format=jpg&name=small"

# Generate QR
url = pyqrcode.create(msj)

# Save SVG
url.svg("myqr.svg", scale=8)

# PNG
url.png("myqr.png", scale=6)
