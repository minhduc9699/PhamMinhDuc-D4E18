# Dictionary

person = [
    'Đức', 
    96, 
    70, 
    75
] # list

person = {
    'key': 'value',
    'name': 'Đức', 
    'yob': 96, 
    'weight': 70, 
    'height': 75,
    'name': 'not Đức'
} # Dict Container 
# C R U D

R 
print(person['name'])
for key in person:
    print(key, person[key])

# C
person['job'] = 'Dev'
for key in person:
    print(key, person[key])
print('------')
# U
person['job'] = 'culi'
for key in person:
    print(key, person[key])
# D
del person['jobbb']
print(person)

# check if key exists
if 'name' in person:
    print(person['name'])