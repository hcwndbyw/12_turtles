from Tkinter import *
import turtle
import datetime

xCoor = 400
yCoor = 300

def _init():
    root = Tk()
    menubar = Menu(root)
    menubar.add_command(label="Save", command=save_image) 
    menubar.add_command(label="Clear", command=_clear)
    root.config(menu=menubar)
    turtle.speed(0)
    turtle.delay(0)
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
def save_image():
    fn = datetime.datetime.now()
    screen = turtle.getscreen()
    screen.getcanvas().postscript(file=fn)

def _clear():
    turtle.reset()
    turtle.bgcolor('white')

   

