import turtle
rammus = turtle.Turtle()
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
def simple_circle(rad):
    rammus.circle(rad)
def circlenostep(rad,ext):
    rammus.circle(rad,ext)
def circle(rad,ext,step):
    rammus.circle(rad,ext,step)
def setposition(x, y):
    rammus.setposition(x, y)
def speed(sped):
    rammus.speed(sped)
def color(color):
    rammus.color(color)
def pensize(size):
    rammus.pensize(size)
def begin_fill():
    rammus.begin_fill()
def end_fill():
    rammus.end_fill()
speed(0)

# example 1
"""
This code will draw 9 shapes in a line, increasing from 0 points to 9.
"""
'''speed(5)
# Send Tracy to starting position
penup()
setposition(-180,0)
# Draw shapes where i controls the number of points and then move forward
for i in range(10):
    pendown()
    circle(20,360,i)
    penup()
    forward(40)'''

# 2.14.4
'''
For loop that makes circle with increasingly larger circle radii and points
'''
radius = 20
for i in range(99):
    if(i > 0):
        pendown()
        circle(radius,360,i)
    else:
        penup()
        setposition(-200,-200)
        setposition(0,0)
        pendown()
    penup()
    setposition(0,0)
    radius += 20
