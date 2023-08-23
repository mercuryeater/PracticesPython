import operations as o
from paquete import sumador, restador
import paquete.sumador.suma as suma
import paquete.restador.resta as resta
import pprint


def main():
    sumRes = o.sum(2, 7)
    sustractRes = o.sustract(5, 2)
    print(f'En main y el resultado de sum es: {sumRes}')
    print(f'En main y el resultado de sustract es: {sustractRes}')
    print(f'Esto es suma: {suma.suma(2,2)}')
    print(f'Esto es resta: {resta.resta(3,2)}')

    resSumPack = sumador.suma.suma(2, 2)
    resRestaPack = restador.resta.resta(3, 2)
    print(f'Suma: {resSumPack} Resta: {resRestaPack}')


if __name__ == '__main__':
    main()


def pruebaLocals(initial):
    value = 3
    state = False
    pprint.pprint(f'Esto es init: {initial}, esto es value: {value}, el estado es {state}')
    pprint.pprint(locals())

pruebaLocals(1)
