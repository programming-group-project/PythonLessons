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
def speed(sped):
    rammus.speed(sped)

# example 1
"""
This code will have Tracy draw an x and y-axis on our screen with
hash marks every 25 pixels.
"""
'''speed(5)
# This function will draw a line with hash marks at every 25 pixels.
def draw_hashed_axis():
    pendown()
    for i in range(16):
        forward(25)
        right(90)
        forward(10)
        backward(20)
        forward(10)
        left(90)
       
# Move Tracy to top of canvas and call draw hash marks function for y-axis.
# Then move Tracy to left of canvas and call hash marks function for x-axis.
penup()
setposition(0,200)
right(90)
draw_hashed_axis()
penup()
setposition(-200,0)
left(90)
draw_hashed_axis()'''

# 2.8.4
'''def draw_bead():    
    penup()
    forward(100)
    right(90)
    pendown()
    circle(10)
    penup()
    setposition(0,0)
    right(2.555555555555555)
right(90)
for i in range(36):
    draw_bead()'''

# 2.8.5
def draw_square():
    backward(25)
    pendown()
    for i in range(4):
        forward(50)
        left(90)
    penup()
    forward(25)
def draw_circle():
    pendown()
    circle(25)
    penup()
def draw_row():
    for i in range(4):
        draw_square()
        forward(50)
        draw_circle()
        forward(50)
height = -200
penup()
for i in range(8):
    setposition(-200, height)
    forward(25)
    draw_row()
    height = height + 50
