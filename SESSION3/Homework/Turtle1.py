from turtle import *

shape("turtle")

speed(5)

colors = ['red', 'blue', 'brown', 'yellow', 'grey']

def polygon(n, side_length):
    for i in range(n):
        lt(360/n)
        fd(side_length)

a = 2
for i in colors:
    color(i)
    a += 1
    polygon(a, 200)


mainloop()