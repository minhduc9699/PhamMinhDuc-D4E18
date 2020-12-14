list = ['a', 2, True]
nested_list = [
    ['-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['-', '-', 'P', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-'],
]
for y in range(len(nested_list)):
    for x in range(len(nested_list[y])):
        print(nested_list[y][x], end=' ')
    print()