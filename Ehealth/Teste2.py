from bs4 import BeautifulSoup
import re
import urllib

page3 = urllib.urlopen("https://angel.co/uber").read()
soup3 = BeautifulSoup(page3)

desc = soup3.findAll(attrs={"name": re.compile(r"description", re.I)}) 
print(desc[0]['content'].encode('utf-8'))