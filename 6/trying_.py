from turtle import *

speed(50)
shape('turtle')
color('green')
left(90)

for i in range(2):
    right(120)
    forward(7*30)

right(300)

for i in range(2):
    right(120)
    forward(7*30)

up()
for x in range(-8, 8):
    for y in range(-8, 1):
        goto(x*30, y*30)
        dot(5, 'red')
done()
