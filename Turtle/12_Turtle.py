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
The color of each hash mark will be determined from user input.
"""

'''# Set initial value of length variable to 25
speed(5)
length = 25

# This function will ask the user for a color.
# It will then draw a hash mark of that color.
def draw_hash_mark():
    color(color_choice)
    pensize(mark_thickness)
    left(90)
    forward(25)
    backward(50)
    forward(25)
    right(90)
    color("black")
    pensize(1)

# Send Tracy to starting position
penup()
setposition(-200,0)
pendown()
mark_thickness=int(input("What is the thickness of the marks? (1-20): "))

# Move Tracy forward by the value of 'length' and draw a hash mark
# Repeat this 4 times, doubling the length each time
for i in range(4):
    forward(length)
    color_choice = input("What color should this mark be?: ")
    draw_hash_mark()
    length = length * 2'''

# 2.12.4

radius = 75
penup()
setposition(0,-100)
left(90)
for i in range(4):
    penup()
    forward(25)
    right(90)
    pendown()
    color_choice = input("What color should this cirle be?: ")
    color(color_choice)
    begin_fill()
    simple_circle(radius)
    end_fill()
    left(90)
    radius -= 25

# 2.12.5
'''square_length = int(input("How big should the square be?: "))
def draw_square():
    for i in range(4):
        pendown()
        forward(square_length)
        left(90)
        penup()
penup()
setposition(-200,-200)
draw_square()
setposition(200 - square_length,-200)
draw_square()
setposition(200 - square_length, 200 - square_length)
draw_square()
setposition(-200, 200 - square_length)
draw_square()'''