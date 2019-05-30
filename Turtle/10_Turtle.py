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
This code will fill the canvas with light blue circles.
"""
'''speed(0)

# This function will draw a row of 10 circles.
def draw_circle_row():
    for i in range(10):
        pendown()
        begin_fill()
        color("light blue")
        simple_circle(20)
        end_fill()
        penup()
        forward(40)
        
def move_up_a_row():
    left(90)
    forward(40)
    right(90)
    backward(400)
    
# Send Tracy to starting position in bottom left corner.
penup()
setposition(-180,-200)

# Call circle drawing function
for i in range(10):
    draw_circle_row()
    move_up_a_row()'''

# 2.10.4
"""
This code will fill the canvas with light blue circles.
"""
'''def draw_circle_row():
    for i in range(10):
        pendown()
        begin_fill()
        color("light blue")
        simple_circle(20)
        end_fill()
        penup()
        left(60)
        forward(30)
        begin_fill()
        color("white")
        pendown()
        simple_circle(5)
        end_fill()
        penup()
        backward(30)
        right(60)
        forward(40)
def move_up_a_row():
    left(90)
    forward(40)
    right(90)
    backward(400)
    
penup()
setposition(-180,-200)

for i in range(10):
    draw_circle_row()
    move_up_a_row()'''

# 2.10.5
'''
    1st function: will make a side (parameter)
    and then turn left 90
    2nd function: will draw a square using the first function
    then trace the outside using it again
'''
def tile(paint,pen):
    color(paint)
    pensize(pen)
    for i in range(4):
        forward(50)
        left(90)
def sidewalk_square():
    pendown()
    begin_fill()
    tile("grey",1)
    end_fill()
    tile("black",2)
    penup()
    forward(50)
penup()
setposition(-150,-200)
for i in range(4):
    for i in range(7):
        sidewalk_square()
    left(90)
    forward(50)