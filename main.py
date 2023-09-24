from tkinter import *
from time import strftime

root = Tk()
root.title("Clock")
root.geometry("525x100")

def time():
    string = strftime("%H:%M:%S %p")
    label.config(text=string)
    label.after(1000, time)

framel = Frame(root, width=525, height=100, bg="black").place(x=0,y=0)

label = Label(framel, font=("ds-digital", 80), background="black", foreground="cyan")
label.pack(anchor="center")

time()

root.mainloop()