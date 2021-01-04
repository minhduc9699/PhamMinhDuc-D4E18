import pymysql
import pyexcel


def init_connection():
    vg_data = pyexcel.get_records(file_name='vgsales.csv')

    client = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='@gmail.com',
        cursorclass=pymysql.cursors.DictCursor
    )

    board = client.cursor()
    return [vg_data, client, board]
