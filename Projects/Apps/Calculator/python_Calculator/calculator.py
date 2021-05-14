from tkinter import *
from tkinter import ttk
global dEquation
global answer
answer = ""
dEquation = ""

root = Tk( )

def bu1():
    dEquation = dEquation + "1"
def bu2():
    dEquation = dEquation + "2"
def bu3():
    dEquation = dEquation + "3"
def bu4():
    dEquation = dEquation + "4"
def bu5():
    dEquation = dEquation + "5"
def bu6():
    dEquation = dEquation + "6"
def bu7():
    dEquation = dEquation + "7"
def bu8():
    dEquation = dEquation + "8"
def bu9():
    dEquation = dEquation + "9"
def bu0():
    dEquation = dEquation + "0"

def addbu():
    dEquation = dEquation + " + "
def subbu():
    dEquation = dEquation + " - "
def mulbu():
    dEquation = dEquation + " * "
def divbu():
    dEquation = dEquation + " / "

def delbu():
    print("delbu")
def okbu():
    print("ok")
    print("Calculating")
    try:
        answer = exec(dEquation)
    except:
        print("error!")

ttk.Label(root, text =answer,foreground="black",font=("Helvetica", 6), background="white").grid(row="0")
Button(root, text = '1', command = bu1, width=2, height=1, bg="red", fg="white").grid(column="1", row = "3")
Button(root, text = '2', command = bu2, width=2, height=1, bg="red", fg="white").grid(column="2", row = "3")
Button(root, text = '3', command = bu3, width=2, height=1, bg="red", fg="white").grid(column="3", row = "3")
Button(root, text = '4', command = bu4, width=2, height=1, bg="red", fg="white").grid(column="1", row = "2")
Button(root, text = '5', command = bu5, width=2, height=1, bg="red", fg="white").grid(column="2", row = "2")
Button(root, text = '6', command = bu6, width=2, height=1, bg="red", fg="white").grid(column="3", row = "2")
Button(root, text = '7', command = bu7, width=2, height=1, bg="red", fg="white").grid(column="1", row = "1")
Button(root, text = '8', command = bu8, width=2, height=1, bg="red", fg="white").grid(column="2", row = "1")
Button(root, text = '9', command = bu9, width=2, height=1, bg="red", fg="white").grid(column="3", row = "1")
Button(root, text = '0', command = bu0, width=2, height=1, bg="red", fg="white").grid(column="1", row = "4")
Button(root, text = '+', command = addbu, width=2, height=1, bg="red", fg="white").grid(column="4", row = "1")
Button(root, text = '-', command = subbu, width=2, height=1, bg="red", fg="white").grid(column="4", row = "2")
Button(root, text = 'x', command = mulbu, width=2, height=1, bg="red", fg="white").grid(column="4", row = "3")
Button(root, text = '\u00f7', command = divbu, width=2, height=1, bg="red", fg="white").grid(column="4", row = "4")
Button(root, text = '\u27f5', command = delbu, width=2, height=1, bg="red", fg="white").grid(column="2", row = "4")
Button(root, text = '\u2713', command = okbu, width=2, height=1, bg="red", fg="white").grid(column="3", row = "4")

root.geometry("75x125")
root.mainloop()