
from Tkinter import *
import turtle


def giveCommand(command):
    turtleCommand = "turtle."+command
    try:
        eval(turtleCommand)
    except Exception:
        print("Received a bad command: "+command)
        pass

"""
filename fn will be an .eps file
"""
def saveImage(fn):
    screen = turtle.getscreen()
    screen.getcanvas().postscript(file=fn)
    

