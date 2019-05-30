import turtle
rammus = turtle.Turtle()
def dash(dist):
    rammus.pendown()
    rammus.forward(dist)
    rammus.penup()
    rammus.forward(dist)
#example 1
'''rammus.penup()
rammus.backward(200)
rammus.pendown()
rammus.forward(100)
rammus.penup()
rammus.forward(100)
rammus.pendown()
rammus.forward(100)
rammus.penup()
rammus.forward(100)
rammus.pendown()'''
rammus.penup()
rammus.backward(200)
dash(50)
dash(50)
dash(50)
dash(50)

