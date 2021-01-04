from connect import init_connection

connection = init_connection()

vg_data = connection[0]
client = connection[1]
board = connection[2]

board.execute('''SELECT * FROM `vgsales`.`region`''')
region_list = board.fetchall()
for i in range(len(vg_data)):
    video_game_name = vg_data[i]['Name']
    board.execute(f''' 
        SELECT * FROM `vgsales`.`video_game`
        WHERE name = "{video_game_name}"
    ''')
    video_game_found = board.fetchone()
    if video_game_found != None:
        video_game_id = video_game_found['id']
        for j in range(len(region_list)):
            region = region_list[j]['name']
            region_id = region_list[j]['id']
            video_game_sales = vg_data[i][region]
            board.execute(f'''
                INSERT INTO `vgsales`.`video_game_sales`(
                    video_game_id,
                    region_id,
                    sales
                ) VALUES (
                    {video_game_id},
                    {region_id},
                    {video_game_sales}
                )
            ''')
client.commit()