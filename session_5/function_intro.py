outside = 'outside'
def say_hello(name, age=16): # define function
    # print(outside)
    variable_something = f'{name}, {age}'
    return variable_something
    

variable = say_hello('D4E18') # call function
print(variable)

variable_2 = say_hello('D4E19', 18)
print(variable_2)


# say_hello('D4E19', 18)

# Scope