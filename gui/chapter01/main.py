#!/usr/bin/env python3
# This sets an association between the file you're writing and Python.
'''
Triple single quote is documentation string used to define what
the python file is use for/ meant to do
'''

import tkinter as tk
from tkinter import ttk

win = tk.Tk()

win.title("Pythin GUI  -- Chapter01")
## win.resizable(False, False)

#ttk.Label(win, text="A Label").grid(column=0, row=0)

aLabel = ttk.Label(win, text="A Label")
aLabel.grid(column=0, row=1)

clicked = True

def click_me():
    action.configure(text="I have been clicked")
    aLabel.configure(foreground='red')
    aLabel.configure(text='A Red lable')

action = ttk.Button(win, text="Click Me", command=click_me)
action.grid(column=1, row=1)

def click_me2():
    action2.configure(text='Hello ' + name.get())

ttk.Label(win, text="Enter Name").grid(column=0, row=2)

action2 = ttk.Button(win, text="Click Me", command=click_me2)
action2.grid(column=1, row=2)

name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=0)

name_entered.focus()





win.mainloop()
