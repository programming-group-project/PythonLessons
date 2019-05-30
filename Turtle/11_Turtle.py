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
This code will draw hash marks at 25, 50, 100, and 200 pixels.
"""
'''
# Set initial value of length variable to 25
speed(5)
length = 25

# This function will draw a hash mark
def draw_hash_mark():
    left(90)
    forward(25)
    backward(50)
    forward(25)
    right(90)

# Send Tracy to starting position
penup()
setposition(-200,0)
pendown()

# Move Tracy forward by the value of 'length' and draw a hash mark
# Repeat this 4 times, doubling the length each time
for i in range(4):
    forward(length)
    draw_hash_mark()
    length = length * 2
'''
# 2.11.4
'''radius = 25
right(90)
for i in range(4):
    penup()
    forward(25)
    left(90)
    pendown()
    simple_circle(radius)
    right(90)
    radius += 25'''

# 2.11.5
'''
Function to draw square then a for loop to draw 5 squares spaced out by the previous length
'''
length = 10
def square(length):
    for i in range(4):
        forward(length)
        left(90)
penup()
setposition(-150,0)
for i in range(5):
    pendown()
    square(length)
    penup()
    forward(length*2)
    length += 10
