from querries import add_category
from querries import category_search
from querries import item_search
from querries import item_purchase
from querries import item_add
from querries import greeting
from querries import purchase

options = [
    {
        'code': 0,
        'name': 'Buy',
    },
    {
        'code': 1,
        'name': 'Add Category',
    },
    {
        'code': 2,
        'name': 'Add Items',
    },
]

greeting()

for i in options:
    print(f"Option Name: {i['name']} - Code: {i['code']}")

print('-' * 34)

query = int(input("Enter the code number of the option you want to get: "))
sel = query

for i in options:
    if query == i['code']:
        option = i
        print(f"Great, you select: {i['name']}")
        print('-' * 34)
    pass

if sel == 0:
    print('There is the items, you can buy: ')
    category_search()
    purchase()
    print('-' * 34)
elif sel == 1:
    add_category()
    print('-' * 34)
elif sel == 2:
    print('Here are the products you can add: ')
    category_search()
    item_add()
    print('-' * 34)
pass