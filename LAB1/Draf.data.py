from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
# 1. Tạo một kết nôi Create conection
url = "https://dantri.com.vn"
conn = urlopen(url)

# 2. Download page
raw_data = conn.read()

page_content  = raw_data.decode("utf8")

# print(page_content)
# 3. Find ro Region of interest
soup = BeautifulSoup(page_content, "html.parser")
ul = soup.find("ul", "ul1 ulnew")

# 4. Extra ROI
li_list = ul.find_all("li")

# print(li_list)
news_list = []
for li in li_list:
    h4 = li.h4
    a = h4.a
    link = url + a["href"]
    title = a.string
    news = {
        "link": link,
        "title": title
    }
    news_list.append(news)
    print(link)

    print(title)

# print(li)
# print(ul.prettify())
# print(soup.prettify())
# 5. Save
pyexcel.save_as(records=news_list, dest_file_name="your_file.xlsx")