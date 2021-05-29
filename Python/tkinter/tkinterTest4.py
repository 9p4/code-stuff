from tkinter import *
from tkinter import messagebox
root = Tk()
def myThing(event=None):
    print("This works")
root.bind_all("<Control-m>", myThing)
input()
myThing()
root.mainloop()