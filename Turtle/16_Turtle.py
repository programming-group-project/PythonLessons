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
This code will have Tracy draw an x and y-axis on our screen. Every other hash
mark will be bolded.
"""
'''speed(5)
# This function will draw a line with hash marks at every 25 pixels. The variable
# 'count' increases each time the loop iterates and changes the thickness of the pen
# based on the count value.
def hash_marks():
    count = 0
    for i in range(16):
        pendown()
        forward(25)
        right(90)
        if count % 2 == 0:
            pensize(5)
        forward(10)
        backward(20)
        forward(10)
        pensize(1)
        left(90)
        penup()
        count = count + 1
# Move Tracy to starting position and then call hash marks function
penup()
setposition(0,200)
right(90)
hash_marks()
setposition(-200,0)
left(90)
hash_marks()'''

# 2.16.4
'''def smile_circle(x,y,size,col,full):
    penup()
    setposition(x,y)
    pendown()
    color(col)
    if(full == "true"):
        begin_fill()
        simple_circle(size)
        end_fill()
    elif(full == "false"):
        circlenostep(size,180)
    penup()

user_happy = input("Are you happy?:")
if(user_happy == "yes"):
    smile_circle(0,-100,100,"yellow","true")
    smile_circle(-50,10,20,"black","true")
    smile_circle(50,10,20,"black","true")
    right(90)
    smile_circle(-80,0,80,"black","false")
'''
# 2.16.5
'''
function that will make sqaure, will fill based on the parameter
'''
def square(col):
    color("black")
    if(col == "white"):
        for i in range(4):
            forward(50)
            left(90)
        forward(50)
    elif(col == "black"):
        begin_fill()
        for i in range(4):
            forward(50)
            left(90)
        end_fill()
        forward(50)
for i in range(6):
    if((i % 2) == 0):
        square("white")
    else:
        square("black")
    