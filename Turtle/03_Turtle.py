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
#example 1
'''forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)'''
#example 2
'''penup()
left(90)
forward(200)
right(90)
right(90)
pendown()
forward(400)
penup()
right(90)
forward(200)
right(90)
forward(200)
right(90)
pendown()
forward(400)'''
#2.3.5
'''forward(50)
left(90)
forward(100)
left(90)
forward(50)
left(90)
forward(100)
left(90)'''
def loop():
    pendown()
    forward(400)
    backward(400)
    penup()
    right(90)
    forward(100)
    left(90)
#2.3.6
penup()
backward(200)
left(90)
backward(200)
right(90)
forward(100)
left(90)
loop()
loop()
loop()
