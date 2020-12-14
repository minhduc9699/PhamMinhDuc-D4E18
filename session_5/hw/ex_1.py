input_string = input('Enter your full name: ')

def standardize_name(string):
    string = string.lower().strip()
    list_string = string.split(' ')
    result = ''
    for i in range(len(list_string)):
        if list_string[i] != '':
            list_string[i] = list_string[i].capitalize()
            result += list_string[i] + ' '
    return result

full_name = standardize_name(input_string)
print(full_name)