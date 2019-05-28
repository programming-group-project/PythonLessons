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
def clear():
    rammus.clear()
speed(0)

# example 1
"""
This code will ask the user how many blocks they want on the bottom of the pyramid
and then draw a pyramid of squares, subtracting one block from each row.
"""
'''# Set row value to 0
speed(0)
row_value=0
# This function moves to next row with x-value based on how many blocks are to
# be placed and the y-value based on the row number (gets 50 pixels higher each row)    
def move_to_row(num_blocks):
    x_value = -((num_blocks*50)/2)
    y_value = -200+(50*row_value)
    penup()
    setposition(x_value,y_value)
    pendown()
# This function draw a row of blocks based on user value    
def draw_block_row(num_blocks):
    for i in range(num_blocks):
        for i in range(4):
            forward(50)
            left(90)
        forward(50)
# Ask the user how many blocks should be on bottom row        
num_blocks=int(input("How many blocks on the bottom row? (8 or less): "))
# Call function to move Tracy to beginning of row position and then increase row
# variable value. Then Tracy will draw the row of blocks needed and subtract one
# from the num blocks variable.
for i in range(num_blocks):
    move_to_row(num_blocks)
    row_value=row_value+1
    draw_block_row(num_blocks)
    num_blocks=num_blocks-1'''

# 2.19.4
'''def markCheck():
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
def arrow():
    pendown()
    forward(100)
    left(45)
    backward(20)
    forward(20)
    right(90)
    backward(20)
    forward(20)
    right(45)
    penup()
def arrowDirect(direction):
    if(direction == "up"):
        setposition(0,-50)
        left(90)
        arrow()
    elif(direction == "down"):
        setposition(0,50)
        right(90)
        arrow()
        left(180)
user_input = int(input("Pick a numbr 1-10:"))
loop = 1
while(loop == 1):
    if(user_input == 2):
        clear()
        markCheck()
        loop = 2
    elif(user_input > 2):
        clear()
        arrowDirect("down")
        user_input = int(input("Pick a numbr 1-10:"))
    elif(user_input < 2):
        clear()
        arrowDirect("up")
        user_input = int(input("Pick a numbr 1-10:"))'''

# 2.19.5
'''radius = 25
user_input = int(input("How many circles should be on the botton?"))
height = -user_input*25
def draw_circle():
    penup()
    forward(radius)
    pendown()
    simple_circle(radius)
    penup()
    forward(radius)
    pendown()
def draw_row(number):
    for i in range(number):
        draw_circle()
def draw_pyramid(input,count, tall):
    for i in range(user_input):
        penup()
        setposition(-count*25,tall)
        pendown()
        draw_row(count)
        count -= 1
        tall += 50
draw_pyramid(user_input,user_input,height)'''

# 2.19.6
'''
function that draws and fills a sqaure based on a parameter
2 fucntions that creates rows, 1 that starts black 1 that starts red
for loop to fill canvas
'''
def square(col):
    color(col)
    begin_fill()
    for i in range(4):
        forward(40)
        left(90)
    end_fill()
    forward(40)

def row1():
    for i in range(5):
        square("red")
        square("black")

def row2():
    for i in range(5):
        square("black")
        square("red")

height = -200
penup()
for i in range(5):
    setposition(-200,height)
    pendown()
    row1()
    height += 40
    penup()
    setposition(-200,height)
    pendown()
    row2()
    height += 40
    penup()