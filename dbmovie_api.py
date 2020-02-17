# -*- coding: utf-8 -*-
import requests, json
import os
import threading
from multiprocessing.pool import ThreadPool

def write_essential(name,id,count='50'):
	url = 'https://douban.uieee.com/v2/movie/celebrity/'+id+'/works?start=1&count='+count
	response = requests.get(url, headers = headers)
	content = json.loads(response.text)

	data = json.dumps(content,ensure_ascii=False,indent =2)
	with open(name,'w',encoding='utf-8') as f:
		f.write(data)

def db_write(name,id,count='50'):
	try:
		file_name = name + id +'.json'

		if file_name not in file_list:
			write_essential(name=file_name, id=id)
			
	except TypeError as e:
		print (name)

def db_extract(file):
	with open(file,'r',encoding='utf8') as f:
		data = json.load(f)
	works_num = data['total']
	## 如果作品超过51部，需要再获取作品数据
	if works_num > 51:
		print('--------------%s--More than 51----------' % celeb_name)
		# write_essential(file ,celeb_dbid,count=str(works_num))

	celeb_name = data['celebrity']['name']
	celeb_name_en = data['celebrity']['name_en']
	celeb_dbid = data['celebrity']['id']
	works = data['works']
	for work in works:
		casts = work['subject']['casts']
		directors = work['subject']['directors']
		for cast in casts:
			name = cast['name']
			dbid = cast['id']
			db_write(name,dbid)
		for director in directors:
			name = director['name']
			dbid = director['id']
			db_write(name,dbid)			

if __name__ == '__main__':
	#获取当前路径
	cwd = os.getcwd()
	file_path = cwd+'\\data'
	new_cwd = os.chdir(file_path)
	file_list = os.listdir(file_path)
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
	## 限制线程数为5
	# sem = threading.Semaphore(5)
	# with sem:
	pool = ThreadPool(processes = 10)
	pool.map(db_extract,(file for file in file_list))
	pool.close()
		# for file in file_list:
			# sem.acquire()
			# t1 = threading.Thread(target =db_extract, args = (file,))
			# t1.start()
			# sem.release()
			# db_extract(file)