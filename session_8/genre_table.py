from connect import init_connection

connection = init_connection()

vg_data = connection[0]
client = connection[1]
board = connection[2]

for i in range(len(vg_data)):
    genre_name = vg_data[i]["Genre"]
    board.execute(f'''
        SELECT * FROM `vgsales`.`genre`
        WHERE name = '{genre_name}'
    ''')
    genre_found = board.fetchone()
    if genre_found == None:
        board.execute(f'''
            INSERT INTO `vgsales`.`genre` (
                id,
                name
            ) VALUES (
                {i},
                '{genre_name}'
            )
        ''')
client.commit()
