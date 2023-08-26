import tkinter
from tkinter import ttk
import sys

window = tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(0, weight=3)


frame = ttk.Frame(window)

label = ttk.Label(frame, text='Hello, world', background='orange')
label.grid(column=0, row=0, sticky=tkinter.W, padx=30, pady=30)

frame.grid(column=0, row=0, sticky=tkinter.W)

# LISTA
# Elemento LISTBOX
list = ['Windows', 'Linux', 'Mac', 'SomeOS']
listChangedForTkInter = tkinter.StringVar(value=list)
listbox = tkinter.Listbox(
    window, listvariable=listChangedForTkInter)
listbox.grid(column=1, row=0, sticky=tkinter.E, padx=30, pady=30)

window.mainloop()

sys.exit(0)
