from tkinter import Tk
from tkinter import Label
import time

root = Tk()
root.title("Clock")

def current_time():
    display_time= time.strftime("%I:%M:%S %p")
    digi_clock.configure(text=display_time)
    digi_clock.after(200,current_time)



digi_clock = Label(root,font=("arial",100),bg="blue",fg="white")
digi_clock.pack()

current_time()

root.mainloop()