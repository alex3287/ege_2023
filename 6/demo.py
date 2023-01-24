from turtle import *


shape('turtle')
color('red')
left(90)
for i in range(7):
    forward(10*30)
    right(120)

up()
for x in range(10):
    for y in range(10):
        goto(x*30, y*30)
        dot(6, 'green')
done()
