list_numbers = [1, 6, 8, 1, 2, 1, 5, 6]

count_number = int(input('what number to count? '))
total_number = list_numbers.count(count_number)
print(total_number)

count = 0
for i in range(len(list_numbers)):
    if list_numbers[i] == count_number:
        count += 1
print(count)