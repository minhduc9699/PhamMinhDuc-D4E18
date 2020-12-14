from turtle import *

color('blue')

speed(-1)
current_size = 80
n = 80
current_size = 1
for i in range(n):
    for j in range(4):
        forward(current_size)
        left(90)
    current_size += current_size / n
    print(current_size)
    left()

mainloop()