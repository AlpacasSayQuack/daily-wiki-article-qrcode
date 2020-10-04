from datetime import datetime
import qrcode
import PIL
from PIL import Image

# Grabs today's date and inserts it into stock wikipedia's featured article link
today = datetime.now()
date_format = "%Y%m%d"
inserted_date = today.strftime(date_format)
featured_url = f"https://en.wikipedia.org/wiki/Special:FeedItem/featured/{inserted_date}000000/en"

# Makes Qrcode from wikipedia link and saves it as qr-wiki.png
file_name = 'qr-wiki.png'
qr_code = qrcode.make(featured_url)
qr_code.save(file_name)
