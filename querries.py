import sqlite3

from datetime import date
today = date.today()

# Connecting to a database
connect = sqlite3.connect('Items')
cursor = connect.cursor()

def greeting():
    print('Welcome to Python Venting Machine!')
    print('-' * 34)
    print('Select the option:')

# Function for adding products
def add_category():
    code = int(input('Enter the product code: '))
    name = str(input('Enter the product name: '))
    price = float(input('Enter the product price: '))
    count = int(input('Enter the quantity of the product: '))
    category_list = [code, name, price, count]
    cursor.execute("INSERT INTO items_db VALUES(?, ?, ?, ?);", category_list)
    connect.commit()
    print('Category was added successfully')

# Function to display all products
def category_search():
    cursor.execute("SELECT id, item_name, price FROM items_db")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    pass

# Function for purchase / price check
def item_add():
    item_sel = input('Please type the code of item (1 column): ')
    cursor.execute("SELECT * FROM items_db WHERE id = ? ", (item_sel))
    sel_result = cursor.fetchall()
    print('You select:')
    print(sel_result)
    earn_item = int(input('Enter the quantity of the product you want to add: '))
    cursor.execute('UPDATE items_db SET item_count == ? WHERE id == ?', (earn_item, item_sel))
    connect.commit()
    print(f'You changed the quantity of the product in the machine to: {earn_item}')

def purchase():
    item_sel = input('Please type the code of item (1 column): ')
    cursor.execute("SELECT item_name FROM items_db WHERE id = " + item_sel)
    sel_result = cursor.fetchall()
    print(f'You select: {sel_result}')
    purchase = input('Pay the price of the selected product: ')
    cursor.execute(f"SELECT price FROM items_db WHERE price == {purchase}")
    pur_result = cursor.fetchall()
    print(f"You pay {pur_result}. Have a good day!")
    print(today)

