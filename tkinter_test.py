# import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import Text
import os
import time
import ctypes


list_of_work = {}
user_name = os.getlogin()

# tk setup
root = Tk()
root.title("Homework on Wallpaper!")
folder_path = StringVar()

# not resizeable
root.resizable(width=False, height=False)

def myClick():
    myClick = Label(root, text ="Enter you wallpaper save location folder")
    myClick.grid(row=3)

def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    save_location.delete(1.0,"end")
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    save_location.insert(1.0, filename)
    print(filename)

def saveSubject1():
    global savesubject1
    subject1Detail = detail1.get(1.0,"end")
    print(subject1Detail)
    
def saveSubject2():
    global savesubject2
    subject2Detail = detail2.get(1.0,"end")
    print(subject2Detail)
    
def saveSubject3():
    global savesubject3
    subject3Detail = detail3.get(1.0,"end")
    print(subject3Detail)
    





myLabel1 = Label(root, text="WARNING: THIS PROGRAM WILL CHANGE YOUR WALLPAPER INSTANTLY AFTER IT'S FINISHED. PLS REMEMBER TO RECORD THE OLD WALLPAPER FILE LOCATION")
myLabel2 = Label(root, text="Copyright to Leo Yu")

save_location = Text(root, width=50, height=3)
savelocation = Button(root, text="Browse", command=browse_button)


subject1 = Label(root, text = 'Subject #1')
detail1 = Text(root, width=50, height=5)
detailSubject1 = Button(root, text="Save Subject1", command=saveSubject1)

subject2 = Label(root, text = 'Subject #2')
detail2 = Text(root, width=50, height=5)
detailSubject2 = Button(root, text="SaveSubject2", command=saveSubject2)

subject3 = Label(root, text = 'Subject #3')
detail3 = Text(root, width=50, height=5)
detailSubject3 = Button(root, text="SaveSubject3", command=saveSubject3)



myLabel1.grid()
myLabel2.grid()
myClick()
save_location.grid() # griding the textinput
savelocation.grid()

subject1.grid() # griding the first subject
detail1.grid() # griding the first detail of the subject
detailSubject1.grid()

subject2.grid() # griding the second subject
detail2.grid() # griding the second detail of the subject
detailSubject2.grid()

subject3.grid() # griding the third subject
detail3.grid() # griding the third detail of the subject
detailSubject3.grid()

# window...lise?
root.mainloop()



