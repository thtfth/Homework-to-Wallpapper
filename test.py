#Import the library
from tkinter import *

#Create an object of tkinter window or frame
win = Tk()

#Define the geometry of window
win.geometry("650x250")

#Create an instance of Text Widget
text = Text(win)
text.pack()

win.mainloop()