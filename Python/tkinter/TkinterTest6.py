from tkinter import *
from tkinter import ttk
n = 0
code = 

pics = ["pi", "pie", "pipi", "piepie"]
for diddlyDoot in pics:
    code = code + "    ttk.Label(popup, text=" + '"' + i + '"' + ").grid(column=0, row=" + str(n) + ")" + """
"""
    code = code + """
    ttk.Button(popup, text='""" + i + """', command=lambda: print('""" + i + """')).grid(column=1, row=""" + str(n) + """)
"""
    n = n + 1
    print(n)
code = code + """    ttk.Button(popup, text="Okay", command = popup.destroy).grid()
    popup.mainloop()"""
print(code)
exec(code)
popupmsg()