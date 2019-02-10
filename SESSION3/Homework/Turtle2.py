from turtle import *

shape("turtle")

speed(5)

colors = ['red', 'blue', 'brown', 'yellow', 'grey']

def rectangle(a, b):
        fd(a)
        for i in range(2):
            rt(90)
            fd(b)
            rt(90)
            fd(a)


for i in colors:
    color(i, i)
    begin_fill()
    rectangle(50, 100)
    end_fill()


mainloop()