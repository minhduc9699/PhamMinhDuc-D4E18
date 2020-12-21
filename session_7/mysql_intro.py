import pymysql

client = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='@gmail.com'
)


board = client.cursor()

def create_database():
    board.execute('CREATE DATABASE `from_python`')

def create_table():
    board.execute('''
        CREATE TABLE `from_python`.`table1` (
            customer varchar(255),
            phone varchar(255),
            product varchar(255),
            quantity int(11),
            price decimal(19,2)
        )
    ''')

def insert_row():
    board.execute(f'''
        INSERT INTO `from_python`.`table1` (
            customer,
            phone,
            product,
            quantity,
            price
        ) VALUES (
            'KH1',
            '0941211921',
            'SP1',
            2,
            45.00
        )
    ''')
insert_row()
client.commit()