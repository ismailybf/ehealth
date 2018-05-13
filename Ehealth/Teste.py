import requests
from bs4 import BeautifulSoup




url = 'https://www.google.com.br/search?q=game+of+thr'
response = requests.get(url)
soup = BeautifulSoup(response.text)

metas = soup.find_all('meta')


#print [ meta.attrs['content'] for meta in metas if 'name' in meta.attrs and meta.attrs['name'] == 'description' ]


for meta in metas:
	if 'name' in meta.attrs:
		if meta.attrs['name']=='description':
			print meta.attrs['content']


