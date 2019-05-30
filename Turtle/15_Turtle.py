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
This code will draw a square swirl from the center of the canvas.
"""
'''speed(5)
# Move forward and turn left 10 times. Move 10 pixels further every iteration
for i in range(10,101,10):
    forward(i)
    left(90)'''

# 2.15.4
'''penup()
for i in range(25, 100, 25):
    right(90)
    forward(i)
    left(90)
    pendown()
    simple_circle(i)
    penup()
    left(90)
    forward(i)
    right(90)'''

# 2.15.5
'''
Function that creates a bar with a given parameter
For loop calls function to make full picture
'''
def bar(height):
    for i in range(2):
        forward(10)
        left(90)
        forward(height)
        left(90)
for i in range(10,50,10):
    bar(i)
    penup()
    forward(35)
    pendown()
