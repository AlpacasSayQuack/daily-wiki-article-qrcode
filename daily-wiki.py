from datetime import datetime
import qrcode
import PIL
from PIL import Image

# Grabs today's date and inserts it into stock wikipedia's featured article link
today = datetime.now()
date_format = "%Y%m%d"
inserted_date = today.strftime(date_format)
featured_url = f"https://en.wikipedia.org/wiki/Special:FeedItem/featured/{inserted_date}000000/en"

'''
uncomment the line below (qr_code variable line) to modify the code's properties:
box_size = how many pixels per box
border = how think in boxes the border should be
version = how large the qrcode is.
    1  is the smallest 21 x 21
    40 is the largest 185 x 185
    Note: if code version is too small to store all code
          this value is over written and will scale up to
          required version for the amount of data included
'''
# qr_code = qrcode.QRCode(version=1, box_size =10, border=4)
# Makes Qrcode from wikipedia link and saves it as qr-wiki.png
file_name = 'qr-wiki.png'
qr_code = qrcode.make(featured_url)
qr_code.save(file_name)
