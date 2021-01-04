from connect import init_connection

connection = init_connection()

vg_data = connection[0]
client = connection[1]
board = connection[2]

for i in range(len(vg_data)):
    publisher_name = vg_data[i]["Publisher"]
    print(publisher_name)
    board.execute(f'''
        SELECT * FROM `vgsales`.`publisher`
        WHERE name = "{publisher_name}"
    ''')
    publisher_found = board.fetchone()
    print(publisher_found)
    if publisher_found == None:
        board.execute(f'''
            INSERT INTO `vgsales`.`publisher` (
                id,
                name
            ) VALUES (
                {i},
                "{publisher_name}"
            )
        ''')
client.commit()
