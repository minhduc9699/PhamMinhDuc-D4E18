inventory = {
    'gold': 500,
    'pouch': ['flint', 'twine', 'gemstone'],
    'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

inventory['pocket'] = [
    'seashell', 
    'strange', 
    'berry', 
    'lint'
]

backpack = inventory['backpack']
remove_index = backpack.index('dagger')
backpack.pop(remove_index)
inventory['gold'] += 50
print(inventory)