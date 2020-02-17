import requests
from bs4 import BeautifulSoup, CData
import re
import xml.etree.cElementTree as ET
from lxml import etree
import json
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = 'https://movie.douban.com/subject/1295644/'
"""
url is based on the subject number, i.e. movie id.
This script will return a file with movie info
""" 
response = requests.get(url, headers = headers)

soup = BeautifulSoup(response.text, 'html.parser')

mo = soup.find('div',attrs={'id':'info'})
imdb = mo.find('a', attrs ={'rel':'nofollow'}).get_text()
movie_info = dict(imdb=imdb)


movie_webinfo= soup.find('script',attrs={'type':'application/ld+json'}).get_text()
movie_info.update(json.loads(movie_webinfo))
x_str = json.dumps(movie_info,ensure_ascii=False,indent=2)
with open('test.json','w') as f:
	f.write(x_str)

