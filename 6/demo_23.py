from turtle import *


speed(30)
shape('turtle')
color('green')
left(90)  # обязательно
for i in range(7):
    forward(10*30)
    right(120)

# рисуем точки
up()
for x in range(-5, 6):
    for y in range(-5, 6):
        goto(x*30, y*30)
        dot(7, 'red')

done()