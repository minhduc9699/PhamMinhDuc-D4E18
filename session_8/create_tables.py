from connect import init_connection

connection = init_connection()

board = connection[2]

board.execute('''
    CREATE TABLE `vgsales`.`region` (
        id INT(11) PRIMARY KEY,
        name VARCHAR(255)
    )
''')

board.execute('''
    CREATE TABLE `vgsales`.`video_game_sales`(
        video_game_id INT(11) REFERENCES `vgsales`.`video_game`(id),
        region_id INT(11) REFERENCES `vgsales`.`region`(id),
        sales DECIMAL(19,2)
    )
''')

