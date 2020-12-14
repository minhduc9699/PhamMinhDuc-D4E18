string_number = '001238234'
print(int(string_number))
# list_number = list(string_number)

number = '${0:,}'.format(int(string_number))
print(number)