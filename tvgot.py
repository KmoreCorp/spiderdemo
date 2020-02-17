import requests
from bs4 import BeautifulSoup
import json

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = 'http://api.tvmaze.com/singlesearch/shows?q=game+of+throne&embed=episodes'

response = requests.get(url, headers = headers)

content = json.loads(response.text)
x = json.dumps(content, ensure_ascii=False,indent =2)
with open('got_info.json','w') as f:
	f.write(x)

# print(cele_info.split(' '))