sheeps = [5, 7, 300, 90, 24, 75]

for month in range(5):
    print(f'after one {month + 1} month, here my sheeps size')
    for i in range(len(sheeps)):
        sheeps[i] += 50
    print(sheeps)
    
    print(f'my sheep after sheered')
    max_sheep_index = 0
    for i in range(len(sheeps)):
        if sheeps[i] > sheeps[max_sheep_index]:
            max_sheep_index = i
    sheeps[max_sheep_index] = 8
    print(sheeps)

total = 0
for i in range(len(sheeps)):
    total += sheeps[i]
print(f'after 5 month, my total sheep size is {total}')
print(f'i would get {total * 2}$')