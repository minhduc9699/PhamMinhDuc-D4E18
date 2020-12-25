import pymysql

client = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='@gmail.com',
    cursorclass=pymysql.cursors.DictCursor
)
board = client.cursor()
board.execute('SELECT * FROM `dantri`.`headline`')
data = board.fetchall()
for i in range(len(data)):
    print(data[i]['title'])