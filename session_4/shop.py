shop = ['T-shirt', 'Hoodie']

# C
new_item = input('Enter new stuff')
shop.append(new_item)
print(shop)

# R
for i in range(len(shop)):
    print(f'{i+1}.{shop[i]}')

# U
update_position = int(input('Enter update position: '))
shop[update_position] = input('Enter new item: ')
print(shop)

# D
delete_position = int(input('Enter delete position: '))
shop.pop(delete_position)
print(shop)