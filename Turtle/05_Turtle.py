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

# example 1
'''rammus.speed(5)
left(30)
for i in range(6):
    forward(100)
    backward(100)
    left(60)'''

# example 2
'''rammus.speed(5)
penup()
setposition(-50,-100)
for i in range(2):
    pendown()
    circle(50)
    penup()
    forward(100)
setposition(-50, 0)
for i in range(2):
    pendown()
    circle(50)
    penup()
    forward(100)'''

# 2.5.5
'''for i in range(6):
    forward(50)
    left(60)'''

# 2.5.6
'''left(45)
for i in range(4):
    forward(100)
    backward(100)
    left(90)'''

# 2.5.7
def loop(repeat):
    for i in range(repeat):
        circle(50)
        penup()
        forward(100)
        pendown()
penup()
setposition(-100, -200)
pendown()
loop(3)
penup()
setposition(-50,-100)
pendown()
loop(2)
penup()
setposition(0,0)
pendown()
loop(1)
    

