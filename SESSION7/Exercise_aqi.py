from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
local = input("Địa điểm:")
s = f"https://wind.waqi.info/nsearch/full/{local}?n=1"
url= s
conn=urlopen(url)
raw_data=conn.read()
page_content=raw_data.decode("utf8")

result = json.loads(page_content)

list_1 = result["results"]
list_2 = list_1[0]

print("location:",list_2["n"][0])
print("time:",list_2["s"]["t"][0])
print("AQI:",list_2["s"]["a"])
print("*_"*10)
