import tkinter
from tkinter import ttk

# Creamos una ventana
window = tkinter.Tk()

#
#  GEOMETRIA GRID
#
# Pensar en rejilla, como un excel
# filas y columnas
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)
# REPASAR COMO ES ESTO DE CREAR EL GRID

user_label = ttk.Label(window, text="username:")
user_label.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)

user_entry = ttk.Entry(window)
user_entry.grid(column=1, row=0, sticky=tkinter.E, padx=5, pady=5)

user_label = ttk.Label(window, text="password:")
user_label.grid(column=0, row=1, sticky=tkinter.W, padx=5, pady=5)

user_entry = ttk.Entry(window, show="*")
user_entry.grid(column=1, row=1, sticky=tkinter.E, padx=5, pady=5)

login_button = ttk.Button(window, text="Login")
login_button.grid(column=1, row=3, sticky=tkinter.E)

# Mantenemos la ventana en ejecucuion
# con un loop

window.mainloop()
