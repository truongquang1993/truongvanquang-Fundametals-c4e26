from turtle import *

shape("turtle")
speed(3)

def draw_star(x, y, length):
    penup()
    goto(x, y)
    pendown()
    for i in range(5):
        fd(length)
        rt(144)


draw_star(50, 50, 150)

mainloop()