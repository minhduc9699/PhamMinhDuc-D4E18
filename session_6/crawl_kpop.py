from requests import get
from bs4 import BeautifulSoup
import pyexcel

response = get('https://dbkpop.com/db/all-k-pop-idols')
file = open('kpop.html', 'w', encoding='utf-8')
file.write(response.text)
