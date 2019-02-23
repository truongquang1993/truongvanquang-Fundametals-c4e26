from turtle import *
def draw_square(lenght, clr):
    color(clr)
    for i in range(4):
        fd(lenght)
        lt(360/4)
shape("turtle")
speed(3)

for i in range(30):
    draw_square(i * 5, "red")
    left(17)
    penup()
    forward(i * 2)
    pendown()

mainloop()