from turtle import *

colors = ['red', 'blue', 'brown', 'yellow', 'grey']

color_index = 0
for n in range(5):
    color(colors[color_index])
    begin_fill()
    for i in range(4):
        if i % 2 == 0:
            forward(50)
        else:
            forward(100)
        left(90)
    end_fill()
    color_index += 1
    forward(50)



mainloop()
