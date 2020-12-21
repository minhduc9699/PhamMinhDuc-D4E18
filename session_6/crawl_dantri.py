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

import pymysql
# connect to mysql
client = pymysql.connect(
    host='localhost',
    user='root',
    port=3306,
    password='@gmail.com'
)

board = client.cursor()

# # create database
# board.execute('CREATE DATABASE `dantri`')
# # create table
# board.execute('''CREATE TABLE `dantri`.`headline`(
#     title text(10000),
#     link text(10000)
# )''')
# access data

for i in range(len(data)):
    title = data[i]['title']
    link = data[i]['link']
    # insert rows
    board.execute(f'''
        INSERT INTO `dantri`.`headline` (
            title,
            link
        ) VALUES (
            '{title}',
            '{link}'
        )
    ''')
    print('saved', title)
client.commit()
