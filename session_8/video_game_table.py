from connect import init_connection

connection = init_connection()

vg_data = connection[0]
client = connection[1]
board = connection[2]

for i in range(len(vg_data)):
    video_game_name = vg_data[i]['Name']
    video_game_year = vg_data[i]['Year']
    board.execute(f'''
        SELECT * FROM `vgsales`.`platform`
        WHERE name = "{vg_data[i]['Platform']}"
    ''')
    platform_found = board.fetchone()
    platform_id = platform_found['id']
    board.execute(f'''
        SELECT * FROM `vgsales`.`genre`
        WHERE name = "{vg_data[i]['Genre']}"
    ''')
    genre_found = board.fetchone()
    genre_id = genre_found['id']
    board.execute(f'''
        SELECT * FROM `vgsales`.`publisher`
        WHERE name = "{vg_data[i]['Publisher']}"
    ''')
    publisher_found = board.fetchone()
    publisher_id = publisher_found['id']
    if video_game_year != 'N/A':
        board.execute(f'''
            INSERT INTO `vgsales`.`video_game`(
                id,
                name,
                year,
                platform_id,
                genre_id,
                publisher_id
            ) VALUES (
                {i},
                "{video_game_name}",
                {video_game_year},
                {platform_id},
                {genre_id},
                {publisher_id}
            )
        ''')
client.commit()