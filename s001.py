import requests
from bs4 import BeautifulSoup, CData
import re
import xml.etree.cElementTree as ET
from lxml import etree
import json
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = 'https://movie.douban.com/subject/30462527/'
response = requests.get(url, headers = headers)


# with open('temp.xml','w') as f:
# 	f.write(response.text)
# # print(response.text)
# # print(type(response.text))
# tree = ET.parse('temp.xml')
# root = tree.getroot()
soup = BeautifulSoup(response.text, 'html.parser')
# # # content = response.json()
# # items = soup.find_all('item')
# # # print(items[0])
# # # print(soup.find_all(text=True))
# # # for cd in soup.findAll(text=True):
# # # 	if isinstance(cd, Cdata):
# # # 		print ('CData contents: %r' % cd)
# # tag = 'content:encoded'
# # root = ET.fromstring(response.text)
# # for item in root.xpath("//description"):
# 	# print (item.text)
# for child in root.iter('item'):
# 	print(child.tag, child.text)
movie_info = soup.find('script',attrs={'type':'application/ld+json'}).get_text()
# print(type(movie_info))
x = json.loads(movie_info)
x_str = json.dumps(x,ensure_ascii=False,indent=2)
with open('test2.json','w') as f:
	f.write(x_str)