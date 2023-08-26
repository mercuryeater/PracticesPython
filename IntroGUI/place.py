import tkinter
import random

window = tkinter.Tk()

colors = ['white', 'black', 'red', 'green', 'blue', 'purple']

for x in range(0, 10):
    color = random.randint(0, len(colors)-1)
    color2 = random.randint(0, len(colors)-1)

    label = tkinter.Label(window, text="etiqueta",
                          bg=colors[color], fg=colors[color2])
    label.place(x=random.randint(0, 100), y=random.randint(0, 100))


label_place1 = tkinter.Label(
    window, text="Posicionamiento absoluto", bg="black", fg="white")
label_place1.place(x=10, y=50)

label_place2 = tkinter.Label(
    window, text="Another one", bg="red", fg="white")
label_place2.place(relx=0.5, rely=0.5, relwidth=0.9, anchor='center')

window.mainloop()
