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
from connect import init_connection

connection = init_connection()

vg_data = connection[0]
client = connection[1]
board = connection[2]

# E T L
for i in range(len(vg_data)):
    # EXTRACT
    platform_name = vg_data[i]['Platform']

    # VERYFILE
    board.execute(f'''
        SELECT name FROM `vgsales`.`platform`
        WHERE name = "{platform_name}"
    ''')
    # TRANSFORM
    #...
    platform_found = board.fetchone()
    if platform_found == None:
        # LOAD
        board.execute(f'''
            INSERT INTO `vgsales`.`platform` (
                id, 
                name
            ) VALUES (
                {i},
                "{platform_name}"
            )
        ''')

client.commit()
#