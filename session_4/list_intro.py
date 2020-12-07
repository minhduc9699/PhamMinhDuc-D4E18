list = ['cơm', 'rau'] # container data type
print(list)

# C R U D

# Create
list.append('thịt')
list.append('thịt kho')

print(list)
# Read
print(list[0]) # Read one
first_item = list[0] # Assign
for i in range(len(list)): # Read All
    print(f'{i}.{list[i]}')
# Update
list[0] = 'Phở'
print(list)
# Delete
list.pop(0) # delete by index
deleted_item = list.pop(0) # Delete by index, then assign to a var
print(deleted_item)

# find index by value
item_index = list.index('thịt')
print(list)
# check a value exists in list
if 'bún đậu' in list:
    print(list.index('bún đậu'))
