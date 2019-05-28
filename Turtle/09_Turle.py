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
This program will draw an octagon where each side is a different color.
"""

'''speed(5)
pensize(5)

# Draw one side of shape, then change color and turn 60 degrees before
# drawing next line. Continue for 8 lines to complete hexagon.
color("red")
forward(50)
left(45)
color("orange")
forward(50)
left(45)
color("yellow")
forward(50)
left(45)
color("green")
forward(50)
left(45)
color("blue")
forward(50)
left(45)
color("indigo")
forward(50)
left(45)
color("purple")
forward(50)
left(45)
color("pink")
forward(50)'''

# example 2
"""
This program draws three shapes from the same position. Each shape is a 
different color.
"""

'''speed(5)

# Draws a red circle
color("red")
begin_fill()
simple_circle(75)
end_fill()

# Draws a blue square due to 4 steps
color("blue")
begin_fill()
circle(75,360,4)
end_fill()

# Draws a yellow triangle due to 3 steps
color("yellow")
begin_fill()
circle(75,360,3)
end_fill()'''

# 2.9.5
'''
    2 functions that make a single trianlge and a for loop to draw
    the 4 triangles
'''
'''def triangle_side():
    forward(50)
    left(120)
def draw_trianle():
    pendown()
    color("red")
    triangle_side()
    color("green")
    triangle_side()
    color("blue")
    triangle_side()
    penup()
    forward(50)
penup()
setposition(-100,0)
pendown()
for i in range(4):
    draw_trianle()'''
# 2.9.6
'''
    function that will draw a circle and return to the middle
    , its called by the for loop to complete the circle
'''
'''def draw_bead():    
    penup()
    forward(100)
    right(90)
    pendown()
    simple_circle(10)
    penup()
    setposition(0,0)
    left(80)
right(90)
for i in range(12):
    color("blue")
    draw_bead()
    color("red")
    draw_bead()
    color("purple")
    draw_bead()'''
# 2.9.7
'''
    defines functions that will draw needed shapes then
    draws them at set positions
'''
def red_square(radius):
    color("red")
    begin_fill()
    circle(radius,360,4)
    end_fill()
def blue_circle(radius):
    color("blue")
    begin_fill()
    simple_circle(radius)
    end_fill()
def yellow_semicircle(radius):
    color("yellow")
    begin_fill()
    circlenostep(radius,180)
    left(90)
    forward(radius*2)
    end_fill()
def green_pentagon(radius):
    color("green")
    begin_fill()
    circle(radius,360,5)
    end_fill()
penup()
setposition(100,100)
pendown()
red_square(60)

penup()
setposition(-100,100)
pendown()
blue_circle(60)

penup()
setposition(-100,-100)
pendown()
yellow_semicircle(60)

penup()
setposition(100,-100)
pendown()
left(90)
green_pentagon(60)