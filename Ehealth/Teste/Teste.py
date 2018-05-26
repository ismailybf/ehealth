# -*- coding: utf-8 -*-#


import unicodedata
import Kassandra.Kassandra as ka
import wikipedia as wiki
wiki.set_lang("pt")
import urllib
from bs4 import BeautifulSoup
import googlesearch.googlesearch as gs
import requests
import webbrowser








query = 'quem é o seya'
#ka.get_wikipedia_search(query)

res,url = ka.get_search_google(query, 3)
print res, url



'''
response = gs.GoogleSearch().search(query,3,"pt-br")
results = response.results
for res in results:
	url = res.url
	print google_scrape(url)
	print url
	webbrowser.open(url)

'''	
	
	
	
	
	
	
	