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
def setposition(x, y):
    rammus.setposition(x, y)

# example 1
'''
This program will draw four circles in a square formation at the center of the
canvas. Each circle will have a radius of 50
'''
'''rammus.speed(5)
# Move to bottom left of circle group at position(-50,-100)
penup()
setposition(-50,-100)
# Draw two circles next to each other
for i in range(2):
    pendown()
    circle(50)
    penup()
    forward(100)
# Move to top of circle row at position (-50, 0)
setposition(-50,0)
# Draw two circles next to each other
for i in range(2):
    pendown()
    circle(50)
    penup()
    forward(100)'''

# 2.6.4
'''
    When called this loop will draw a circle.
    The amount of times that it will draw a cirlce is
    based on the parameter, when the parameter is the 
    amount of cirlces
'''
def loop(repeat):
    for i in range(repeat):
        circle(50)
        penup()
        forward(100)
        pendown()
# Set position and do loop 3 times for the bottom row of circles
penup()
setposition(-100, -200)
pendown()
loop(3)
# Set position and do loop 2 times for middle row of circles
penup()
setposition(-50,-100)
pendown()
loop(2)
# Set position and do loop 1 time for top circle
penup()
setposition(0,0)
pendown()
loop(1)