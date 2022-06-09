from tkinter import ttk
from tkinter import *
from tkinter.constants import HORIZONTAL
import tkinter as tk

root = tk.Tk()
root.geometry("500x400")
root.title("My Slider")

mySlider = Scale(
    root,
    from_=0,
    to=100,
    orient=HORIZONTAL,
    tickinterval=50,
)

mySlider.pack()


def new_func(mySlider):
    def myFunc():
        f = open("Rate.txt", "a")
        f.write(f"your rating is : {mySlider.get()}\n")
        f.close()
    return myFunc

myFunc = new_func(mySlider)

ttk.Button(root, text="Rate", command=myFunc).pack()
root.mainloop()
