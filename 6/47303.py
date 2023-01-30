from turtle import *

speed(300)
shape('turtle')
color('red')
left(90)

for i in range(4):
    forward(5*30)
    right(90)
    forward(10*30)
    right(90)

up()
for x in range(12):
    for y in range(7):
        goto(x*30, y*30)
        dot(8, 'green')

done()


# Повтори 4 [Вперёд 5 Направо 90 Вперёд 10 Направо 90]
