# Get the information of Top 250 films in douban.com
# use easy Regular Expression to parse information
import requests
import json
import re
import time

def Get_One_Page(url):
	headers = {
		'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'
	}
	response = requests.get(url,timeout=10,headers=headers)
	if response.status_code == 200:
		return response.text
	else:
		return None

def Parse_One_Page(html):
	pattern = re.compile('<li>.*?em class.*?>(.*?)</em>.*?title.*?>(.*?)</span>.*?<br>.*?([0-9]*?)&.*?average">(.*?)<.*?</li>',re.S)
	items = re.findall(pattern,html)
	# print(items)
	for item in items:
		yield {
			'Ranking': item[0],
			'FileName': item[1],
			'Year': item[2],
			'Stars': item[3]
		}

def Wirte2File(dict_content,FileName):
	with open(FileName,'a',encoding='utf-8') as f:
		f.write(json.dumps(dict_content,ensure_ascii=False)+'\n')

def main(start):
	url = 'https://movie.douban.com/top250?start='+str(start)+'&filter='
	# The path needs to be changed
	FileName = 'E:\onedrive\WorkSpace\Python\Source\doubanTop250.txt'
	for item in Parse_One_Page(Get_One_Page(url)):
		print(item)
		Wirte2File(item,FileName)

if __name__ == '__main__':
	for i in range(10):
		main(i*25)
		