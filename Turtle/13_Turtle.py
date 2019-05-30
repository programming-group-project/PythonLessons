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
This code will draw concentric circles of any size input as parameters.
"""
'''speed(5)
 # This function moves Tracy to the bottom position of a circle based on the radius
 # and then draws the circle around the center before moving back to the center
def draw_circle(radius):
    right(90)
    forward(radius)
    left(90)
    pendown()
    simple_circle(radius)
    penup()
    setposition(0,0)
    
# Ask the user for 3 radiaii and call the draw_circle function with these values
penup()
first_radius = int(input("What is the first circle's radius?: "))
second_radius = int(input("What is the second circle's radius?: "))
third_radius = int(input("What is the third circle's radius?: "))
draw_circle(first_radius)
draw_circle(second_radius)
draw_circle(third_radius)'''

# 2.13.4
'''def body(col):
    pendown()
    color(col)
    begin_fill()
    simple_circle(20)
    end_fill()
    penup()
    forward(40)
penup()
setposition(-100,0)
for i in range(2):
    body("blue")
    body("green")
    body("red")
    body("purple")'''

# 2.12.5
'''circle_radius = int(input("What is the circle's radius?: "))
def square(length):
    color("red")
    begin_fill()
    for i in range(4):
        forward(length)
        left(90)
    end_fill()

def draw_circle(radius):
    color("blue")
    begin_fill()
    simple_circle(radius)
    end_fill()

setposition(-circle_radius,-circle_radius)
square(circle_radius*2)
forward(circle_radius)
draw_circle(circle_radius)'''

# 2.12.6
'''
Makes function that draws a circle and moves to the top to prepare for another circle
all based off of the input variable
'''
snowman_size = int(input("How big is the snowman?:"))
def draw_segment(size):
    color("grey")
    pendown()
    begin_fill()
    simple_circle(size)
    end_fill()
    penup()
    left(90)
    forward(size*2)
    right(90)
penup()
setposition(0,snowman_size*-2)
for i in range(3):
    draw_segment(snowman_size)
    snowman_size = snowman_size / 2