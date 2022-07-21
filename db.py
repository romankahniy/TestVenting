import sqlite3

connect = sqlite3.connect('Items')
cursor = connect.cursor()

connect.execute('''CREATE TABLE IF NOT EXISTS items_db
                (id INT PRIMARY KEY,
                 item_name TEXT,
                 price INT,
                 item_count INT);
''')
connect.commit()

connect.execute('''CREATE TABLE IF NOT EXISTS purchases_db
                (id INT PRIMARY KEY AUTO_INCREMENT,
                 item_id INT,
                 purchase_at DATE);
''')
connect.commit()


