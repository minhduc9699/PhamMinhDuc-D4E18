from random import shuffle
from getpass import getpass

string = getpass('Quiz')
list_string = list(string)
shuffle(string)
print(string)
