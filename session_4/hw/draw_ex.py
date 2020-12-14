from turtle import *

colors = ['red', 'blue', 'brown', 'yellow', 'grey']

color_index = 0
for n in range(3, 8):
    color(colors[color_index])
    for i in range(n):
        forward(100)
        left(360/n)
    color_index += 1

mainloop()