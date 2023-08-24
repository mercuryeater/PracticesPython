import tkinter
import pprint as p

# Creamos una ventana
window = tkinter.Tk()

# Aqui posicionaremos cosas dentro de window
# Primero creamos nuestro primer widget
# .label recibe varios argumentos, primero en que ventana va
# los otros son atributos que puede llevar
# color de fondo, del foreground, que dice el texto
label_saludo = tkinter.Label(window, text="Hello!", bg="orange", fg="white")
label_saludo.pack()

label_bye = tkinter.Label(window, text="Bye", bg="blue", fg="white")
# En el .pack() podemos pasar como argumentos
# padding, por ejemplo el innerpadding en eje x y y
label_bye.pack(ipadx=50, ipady=50)

#
# VOY EN EL MIN 20
#


# Mantenemos la ventana en ejecucuion
# con un loop

window.mainloop()

# print(type(window))
# p.pprint(dir(window))
