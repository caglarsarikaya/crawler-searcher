from general import *
from urllib.parse import urlparse
import  requests
from bs4 import BeautifulSoup
import urllib


word = input("ne aramak istersiniz").lower()
searcher(word)

"""""

from bs4 import BeautifulSoup
import requests

url = "https://bm.erciyes.edu.tr/?Anasayfa"

istek = requests.get(url = url)
html = istek.text
soup = BeautifulSoup(html, 'html.parser')

print(soup.title)
print(soup.title.text)

for i in soup.find_all("meta",{"name":"keywords"}):
    asa = i
    print(asa)

url = "http://www.python.tc/python-kullanim-ozellikleri"
url_oku = urllib.request.urlopen(url)
soup = BeautifulSoup(url_oku, 'html.parser')
print(soup.title.text)

"""

