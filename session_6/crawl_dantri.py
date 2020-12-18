from requests import get
from bs4 import BeautifulSoup
import pyexcel

response = get('https://dantri.com.vn/')
print(response.headers)
file = open('dantri.html', 'w', encoding='utf-8')
file.write(response.text)

# load html to bs4
content_html = BeautifulSoup(response.text)
# find ul tag that contain data
ul_html = content_html.find('ul', {'class': 'dt-list'})
li_html = ul_html.find_all('li')

data = []
for i in range(len(li_html)):
    a_html = li_html[i].find('a')
    title = a_html.text.strip()
    link = a_html['href']
    data.append({
        'title': title,
        'link': link
    })
pyexcel.save_as(dest_file_name='dan_tri.xls', records=data)