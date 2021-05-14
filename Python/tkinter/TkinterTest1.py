import tkinter as tk
import time
counter = 0 
def counter_label(label):
    def count():
        time.sleep(0.1)
        counter += 1
        label.config(text=str(counter))
        label.after(1000, count)
    count()
root = tk.Tk()
root.title("Counting Seconds")
label = tk.Label(root, fg="green")
label.pack()
counter_label(label)
button = tk.Button(root, text='Stop', width=25, command=root.destroy)
button.pack()
root.mainloop()