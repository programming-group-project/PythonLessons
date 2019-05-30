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
This code will have Tracy draw circles from the bottom of the canvas. The first 
circle will have a radius of 10 and the radii will increase by 10 for each. The 
code will stop when the circle reaches a radius value of 200.
"""
'''#Set radius value to 10
speed(0)
radius = 10
#Send Tracy to starting position at bottom middle of canvas
penup()
setposition(0,-200)
pendown()
#While the radius value is less than or equal to 200, draw circles. Increase 
#the radius value by 10 on each iteration.
while radius <= 200:
    simple_circle(radius)
    radius = radius + 10'''

# 2.18.4
'''def draw_square(length):
    pendown()
    for i in range(4):
        forward(length)
        left(90)
size = 50
while(size < 400):
    penup()
    setposition(-size/2,-size/2)
    draw_square(size)
    size += 50'''

# 2.18.5
'''
Function that makes check mark
while loops that will make check mark when the user input is 4
'''
def markCheck():
    color("green")
    penup()
    setposition(0,-50)
    pendown()
    left(45)
    forward(50)
    backward(50)
    left(90)
    forward(25)
    right(135)
user_input = int(input("Pick a numbr 1-10:"))
loop = 1
while(loop == 1):
    if(user_input !=4):
        user_input = int(input("Pick a numbr 1-10:"))
    elif(user_input == 4):
        markCheck()
        loop = 2
