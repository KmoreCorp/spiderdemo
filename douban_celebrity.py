import requests
from bs4 import BeautifulSoup
import json

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = 'https://movie.douban.com/celebrity/1025182/'

response = requests.get(url, headers = headers)

soup = BeautifulSoup(response.text, 'html.parser')

cele_info = soup.find('div', attrs={'class':'item'}).find('ul').find_all('li')
# print(cele_info.strip(' ').strip('\r').strip('\n'))
for i in cele_info:
	b = i.get_text().split()
	print(b)
# print(cele_info.split(' '))