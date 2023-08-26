import tkinter
import pprint as p

# Creamos una ventana
window = tkinter.Tk()

# Aqui posicionaremos cosas dentro de window
# Primero creamos nuestro primer widget
# .label recibe varios argumentos, primero en que ventana va
# los otros son atributos que puede llevar
# color de fondo, del foreground, que dice el texto

label_bye = tkinter.Label(window, text="Bye", bg="blue", fg="white")
#
# GEOMETRIA PACK
#
# En el .pack() podemos pasar como argumentos
# padding, por ejemplo el innerpadding en eje x y y
label_bye.pack(ipadx=50, ipady=50)

# Se puede usar fill para que ocupe todo el espacio, en este
# caso en el eje x
# se puede usar 'x', 'y' y 'both'
label_coco = tkinter.Label(window, text="Coco", bg="orange", fg="white")
label_coco.pack(fill='x', ipady=50)

label_expand = tkinter.Label(window, text="Expand", bg="gray", fg="white")
label_expand.pack(expand=True)

# Hay otros que son de posicionamiento:
label_red = tkinter.Label(window, text="red", bg="red", fg="white")
label_red.pack(side='left', ipady=50)
label_blue = tkinter.Label(window, text="blue", bg="blue", fg="white")
label_blue.pack(side='right', ipady=50)

#
#  GEOMETRIA GRID
#
# Pensar en rejilla, como un excel
# filas y columnas
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)
# Mantenemos la ventana en ejecucuion
# con un loop

window.mainloop()

# print(type(window))
# p.pprint(dir(window))
