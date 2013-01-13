from Tkinter import *
import turtle

xCoor = 400
yCoor = 300

def _init():
    turtle.speed(0)
    turtle.setworldcoordinates(-xCoor,-yCoor,xCoor,yCoor)
    turtle.up()
    turtle.setpos(0,0)
    turtle.down()

def giveCommand(command):
    eval('turtle.'+command)
    if turtle.xcor() < -xCoor or turtle.xcor() > xCoor:
        turtle.setx(0)
    if turtle.ycor() < -yCoor or turtle.ycor() > yCoor:
        turtle.sety(0)

"""
filename fn will be an .eps file
"""
def saveImage(fn):
    screen = turtle.getscreen()
    screen.getcanvas().postscript(file=fn)
    
    

