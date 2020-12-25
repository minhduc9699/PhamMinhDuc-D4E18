# data_game = {
#     'name': 'Wii...',
#     'year': 2007,
#     'Platform_id': {
#         'id': 1,
#         'name': 'Wii',
#     },
#     'Publisher': {
#         'id': 1,
#         'name': 'Nintendo'
#     },
#     'genre': {
#         'id': 1,
#         'name': 'Sports'
#     },
#     'top_players': [
#         {},
#         {}
#     ]
# }
import pymysql

client = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='@gmail.com',
    cursorclass=pymysql.cursors.DictCursor
)

board = client.cursor()

# board.execute('CREATE DATABASE `vgsales`')

# board.execute('''
#     CREATE TABLE `vgsales`.`platform`(
#         id INT(11) PRIMARY KEY,
#         name VARCHAR(255)
#     )
# ''')

board.execute('''
    CREATE TABLE `vgsales`.`video_game` (
        id INT(11) PRIMARY KEY,
        name VARCHAR(255),
        year INT(11),
        platform_id INT(11) REFERENCES `vgsales`.`platform`(id)
    )
''')