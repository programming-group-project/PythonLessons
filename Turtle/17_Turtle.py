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
This program determines if a number is positive, negative, or and then communicates
that to the user by drawing a plus sign, minus sign, or 0.
"""
'''
speed(5)
# This function draws a zero in the middle of the canvas
def draw_zero():
    penup()
    setposition(0,-150)
    pendown()
    circle(50)
# This function draws a minus sign in the middle of the canvas
def draw_minus():
    forward(50)
    backward(100)
    forward(50)
# This function draws a plus sign in the middle of the canvas    
def draw_plus():
    for i in range(4):
        forward(50)
        backward(50)
        left(90)    
# The user is asked to give a number. If they answer with a positive value,
# a plus sign appears. If they answer with a negative value, a minus sign
# appears and if they answer with a 0, a 0 appears.
number = int(input("Enter a number: "))
pensize(10)
color("blue")
if number > 0:
    draw_plus()
elif number < 0:
    draw_minus()
else:
    draw_zero()'''

# 2.17.4
'''
3 functions that will draw marks, if/elif statement that will
call from 1 of the 3 functions based on the user input
'''
'''def markX():
    color("red")
    left(45)
    for i in range(4):
        forward(50)
        backward(50)
        right(90)
    penup()
def markLine():
    color("yellow")
    penup()
    setposition(-50,0)
    pendown()
    forward(100)
    penup()
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
user_input = int(input("Give a rating 1-10:"))
if(user_input >= 8):
    markCheck()
elif(user_input >= 5):
    markLine()
elif(user_input <=4):
    markX()'''

#2.17.5
'''
Function that will make circles based off of the paramters
if/elif statement that will change what it draws based off of user input
'''
def smile_circle(x,y,size,col,full):
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
elif(user_happy == "no"):
    smile_circle(0,-100,100,"yellow","true")
    smile_circle(-50,10,20,"black","true")
    smile_circle(50,10,20,"black","true")
    left(90)
    smile_circle(80,-80,80,"black","false")