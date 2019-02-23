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

color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)

mainloop()