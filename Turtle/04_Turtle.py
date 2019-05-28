import turtle
rammus = turtle.Turtle()
rammus.speed(0)
def forward(dist):
    rammus.forward(dist)
def backward(dist):
    rammus.backward(dist)
def left(dist):
    rammus.left(dist)
def right(dist):
    rammus.right(dist)
def penup():
    rammus.penup()
def pendown():
    rammus.pendown()
def circle(rad):
    rammus.circle(rad)
#example 1
'''for i in range(4):
    forward(50)
    left(90)'''
#example 2
'''penup()
backward(200)
for i in range (40):
    pendown()
    forward(5)
    penup()
    forward(5)'''
#2.4.5
'''penup()
backward(200)
right(90)
for i in range (20):
    pendown()
    circle(10)
    left(90)
    penup()
    forward(20)
    right(90)'''
#2.4.6
penup()
backward(200)
left(90)
backward(200)
right(90)
forward(100)
left(90)
for i in range(3):
    pendown()
    forward(400)
    backward(400)
    penup()
    right(90)
    forward(100)
    left(90)