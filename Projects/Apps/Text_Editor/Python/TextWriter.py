from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import os
import sys
alignment = "left"
root = Tk( )
textGoesHere = Entry(root, width="100", justify=alignment).grid(row=1, column=1, rowspan=10, padx=10, pady=10, columnspan=2)


def newFile:
    open()


menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=newFile)


root.geometry("625x400")
root.configure(background='light blue')
root.mainloop()