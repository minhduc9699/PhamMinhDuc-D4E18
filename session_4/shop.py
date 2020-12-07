shop = ['T-shirt', 'Hoodie']
action = input('welcome to our shop, what do you want? (C R U D): ')

if action == 'C':
    # C
    new_item = input('Enter new stuff')
    shop.append(new_item)
    print(shop)
elif action == 'R':
    # R
    for i in range(len(shop)):
        print(f'{i+1}.{shop[i]}')
elif action == 'U':
    # U
    update_position = int(input('Enter update position: '))
    shop[update_position] = input('Enter new item: ')
    print(shop)
elif action == 'D':
    # D
    delete_position = int(input('Enter delete position: '))
    shop.pop(delete_position)
    print(shop)
