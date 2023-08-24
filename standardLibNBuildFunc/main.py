# Programacion Multihilo
# para multiples funciones en paralelo
import _thread
import time


def currentTime():
    print("Hello World")


_thread.start_new_thread(currentTime, ())
_thread.start_new_thread(currentTime, ())
# No se ejecuta asi cmo asi porque como esta multihilo
# toma cierto tiempo, entonces se puede hacer un loop infinito:
# while True:
#     pass
#  o usar un sleep luego de 1 segundo:
time.sleep(1)
