from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
# 1. Tạo một kết nôi Create conection
url = "https://dantri.com.vn"
conn = urlopen(url)

# 2. Download page
raw_data = conn.read()

page_content  = raw_data.decode("utf8")

with open("dantri.html", "wb") as f:
    f.write(raw_data)