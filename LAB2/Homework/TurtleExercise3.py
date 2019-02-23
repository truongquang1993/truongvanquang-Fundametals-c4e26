from turtle import *
shape("turtle")
speed(5)

def draw_square(lenght, clr):
    color(clr)
    for i in range(4):
        fd(lenght)
        lt(360/4)



mainloop()
