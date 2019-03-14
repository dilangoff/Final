'''
Hi my name is Dilan Goff and this is my finale exam project I made a drawing with turtle graphics and asked the
reviewers about it
'''

import turtle

my_turtle = turtle.Turtle()

# Python program to draw
# Rainbow Benzene
# using Turtle Programming
import turtle

t.speed(0)
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(180):
    t.pencolor(colors[x%6])
    t.width(x/100 + 1)
    t.forward(x)
    t.left(59)

turtle.done()

#This is my code for the survey questions

    like = -5
 while like <1 or like >3:
    try:
        like = float(input('Did you like my Drawing?(1 = yes 2 = No) '))

    except ValueError:
        print('1 or 2')


if like == 1:
    print('Thank you')

if like == 2:
    print('Thank you for your input, I hope you will like are next drawing')



