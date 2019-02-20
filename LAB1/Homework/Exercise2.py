from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
# # 1. Tạo một kết nôi Create conection
url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
conn = urlopen(url)

# # 2. Download page
raw_data = conn.read()

page_content  = raw_data.decode("utf8")

with open("SuaVietNam.html", "wb") as f:
    f.write(raw_data)
# page_content  = f.decode("utf8")

# 3. Find ROI (Region of insert)
soup = BeautifulSoup(page_content, "html.parser")

print(soup, prettify())

# table = soup.find("table", id="tableContent")
# tbody = table.tbody

# print(tbody)


# 4. Extra ROI
# tr_list = tbody.find_all("tr")
# print(li_list)

# title_list = []
# row = []
# clum = []
# for tr in tr_list:
#     td_list = tr.find_all("td")
#     j = 0
#     clum0 = {}
#     for i in td_list[0:5]:
#         cl = i.string
#         j += 1
#         clum0[j]= cl
#     clum.append(clum0)

#     # strong = li.strong
#     # oder_number = strong.string

#     # h3 = li.h3
#     # a = h3.a
#     # link_song = a["href"]
#     # name_song = a.string

#     # h4 = li.h4
#     # aa = h4.a
#     # name_artist = aa.string

#     # top = OrderedDict({
#     #     "oder number": oder_number,
#     #     "link song": link_song,
#     #     "songs'name": name_song,
#     #     "artist": name_artist
#     # })
#     # top_list.append(top)

# # 5. Save
# pyexcel.save_as(records=clum, dest_file_name="Exer2.xlsx")