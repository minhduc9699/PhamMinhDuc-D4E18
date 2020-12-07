from random import shuffle
from getpass import getpass

string = getpass('Quiz')
string = list(string)
shuffle(string)
print(string)
