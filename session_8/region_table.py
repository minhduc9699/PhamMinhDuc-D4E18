from connect import init_connection

connection = init_connection()

vg_data = connection[0]
client = connection[1]
board = connection[2]

count = 0
for key in vg_data[0]:
    if 'Sales' in key:
        board.execute(f'''
            SELECT * FROM `vgsales`.`region`
            WHERE name = "{key}"
        ''')
        region_found = board.fetchone()
        if region_found == None:
            board.execute(f'''
                INSERT INTO `vgsales`.`region`(
                    id,
                    name
                ) VALUES (
                    {count},
                    "{key}"
                )
            ''')
            count += 1
client.commit()