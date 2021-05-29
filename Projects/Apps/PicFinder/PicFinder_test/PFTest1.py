from tkinter import *

root = Tk()

menubar = Menu(root)

helpmenu = Menu(menubar)
nested_menu1 = Menu(helpmenu)
nested_menu1.add_command(label='Stuff 1')
nested_menu1.add_command(label='Stuff 2')

nested_menu2 = Menu(helpmenu)
nested_menu2.add_command(label='Stuff 3')
nested_menu2.add_command(label='Stuff 4')

menu2_nested = Menu(nested_menu2)
menu2_nested.add_command(label='Stuff 5')
nested_menu2.add_cascade(label='Nestception', menu=menu2_nested)

helpmenu.add_cascade(label='1.0 Nested', menu=nested_menu1)
helpmenu.add_cascade(label='2.0 Nested', menu=nested_menu2)

menubar.add_cascade(label="Nested Menus", menu=helpmenu)

root.config(menu=menubar)
root.mainloop()