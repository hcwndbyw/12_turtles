from Tkinter import *
import turtle

xCoor = 800
yCoor = 600

def _init():
    turtle.speed(0)
    turtle.setworldcoordinates(1,0,xCoor,yCoor)
    turtle.up()
    turtle.setpos(xCoor/2,yCoor/2)
    turtle.down()

def giveCommand(command):
    eval('turtle.'+command)
    if turtle.xcor() < 0 or turtle.xcor() > xCoor:
        turtle.setx(xCoor/2)
    if turtle.ycor() < 0 or turtle.ycor() > yCoor:
        turtle.sety(yCoor/2)

"""
filename fn will be an .eps file
"""
def saveImage(fn):
    screen = turtle.getscreen()
    screen.getcanvas().postscript(file=fn)
    

