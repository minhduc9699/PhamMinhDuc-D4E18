from connect import init_connection

connection = init_connection()

board = connection[2]

# board.execute('''
#     CREATE TABLE `vgsales`.`region` (
#         id INT(11) PRIMARY KEY,
#         name VARCHAR(255)
#     )
# ''')

board.execute('''
    CREATE TABLE `vgsales`.`video_game_sales`(
        video_game_id INT(11) REFERENCES `vgsales`.`video_game`(id),
        region_id INT(11) REFERENCES `vgsales`.`region`(id),
        sales DECIMAL(19,2)
    )
''')

# board.execute('CREATE DATABASE `vgsales`')

# board.execute('''
#     CREATE TABLE `vgsales`.`platform`(
#         id INT(11) PRIMARY KEY,
#         name VARCHAR(255)
#     )
# ''')

# board.execute('''
#     CREATE TABLE `vgsales`.`genre`(
#         id INT(11) PRIMARY KEY,
#         name VARCHAR(255)
#     )
# ''')

# board.execute('''
#     CREATE TABLE `vgsales`.`publisher`(
#         id INT(11) PRIMARY KEY,
#         name VARCHAR(255)
#     )
# ''')

# board.execute('''
#     CREATE TABLE `vgsales`.`video_game` (
#         id INT(11) PRIMARY KEY,
#         name VARCHAR(255),
#         year INT(11),
#         platform_id INT(11) REFERENCES `vgsales`.`platform`(id),
#         genre_id INT(11) REFERENCES `vgsales`.`genre`(id),
#         publisher_id INT(11) REFERENCES `vgsales`.`publisher`(id)
#     )
# ''')


