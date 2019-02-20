from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
import pyexcel

from youtube_dl import YoutubeDL

## part 1:
# 1. Tạo một kết nôi Create conection
url = "https://www.apple.com/itunes/charts/songs/"
conn = urlopen(url)

# 2. Download page
raw_data = conn.read()
page_content  = raw_data.decode("utf8")
# print(page_content)
# 3. Find ROI (Region of insert)
soup = BeautifulSoup(page_content, "html.parser")
section = soup.find("section", "section chart-grid")
div = section.find("div", "section-content")
ul = div.find("ul")


# 4. Extra ROI
li_list = ul.find_all("li")
# print(li_list)


top_list = []
for li in li_list[0:10]: #Chọn phần tử trong list Chọn nhỏ thôi làm part 2 cho nhanh ^^
    strong = li.strong
    oder_number = strong.string

    h3 = li.h3
    a = h3.a
    link_song = a["href"]
    name_song = a.string

    h4 = li.h4
    aa = h4.a
    name_artist = aa.string

    top = OrderedDict({
        "oder number": oder_number,
        "link song": link_song,
        "songs'name": name_song,
        "artist": name_artist
    })
    top_list.append(top)
# <Part 2>
    options = {
        "default_search": "ytsearch",
        "max_downloads": 1
    }
    dl = YoutubeDL(options)
    dl.download([name_song])
#</Part 2>

# 5. Save
pyexcel.save_as(records=top_list, dest_file_name="Top songs.xlsx")




