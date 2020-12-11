teencode = {
    'stt': 'so thu tu',
    'pt': 'pee tee'
}

while True:
    for code in teencode:
        print(code, end='\t')
    print()

    input_code = input('your code?')

    if input_code in teencode:
        print(f'trans: {teencode[input_code]}')
    else:
        choice = input('this code not found, wanna contrib? (y/n)')
        choice = choice.lower()
        if choice == 'y':
            input_trans = input('it meaning: ')
            teencode[input_code] = input_trans
        else:
            print('bye bye')
            break