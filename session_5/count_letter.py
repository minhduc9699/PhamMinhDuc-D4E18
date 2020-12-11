def count_letter(letter_to_counts):
    count_letter = {}
    for i in range(len(letter_to_counts)):
        if letter_to_counts[i] != ' ':
            if letter_to_counts[i] in count_letter:
                count_letter[letter_to_counts[i]] += 1
            else:
                count_letter[letter_to_counts[i]] = 1
    return count_letter


string = 'hello'
list_string = list(string)

result = count_letter(list_string)

for key in result:
    print(f'{key} appears {result[key]}')

