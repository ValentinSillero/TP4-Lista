"""
Ejercicio 12 - Eliminar el anteúltimo nodo.

Se resuelve:
1) con lista simplemente enlazada;
2) con lista doblemente enlazada.

Bibliografía:
Walter Bel (2020), Algoritmos y estructuras de datos en Python.
Capítulo VIII - Guía de ejercicios prácticos, pág. 114.
"""

from tda_lista import lista, insertar, barrido
from tda_lista_doble import (
    listaDoble, insertar as insertar_doble,
    barrido as barrido_doble
)


def eliminar_anteultimo_simple(lista_obj):
    if lista_obj.tamanio < 2:
        return None

    # Si hay dos nodos, el anteúltimo es el primero.
    if lista_obj.tamanio == 2:
        dato = lista_obj.inicio.info
        lista_obj.inicio = lista_obj.inicio.sig
        lista_obj.tamanio -= 1
        return dato

    anterior = lista_obj.inicio
    actual = lista_obj.inicio.sig

    # Al terminar, actual será el anteúltimo.
    while actual.sig.sig is not None:
        anterior = actual
        actual = actual.sig

    dato = actual.info
    anterior.sig = actual.sig
    lista_obj.tamanio -= 1
    return dato


def eliminar_anteultimo_doble(lista_obj):
    if lista_obj.tamanio < 2:
        return None

    objetivo = lista_obj.fin.ant
    dato = objetivo.info

    if objetivo.ant is None:
        # Caso de dos nodos: se elimina el inicio.
        lista_obj.inicio = lista_obj.fin
        lista_obj.fin.ant = None
    else:
        objetivo.ant.sig = lista_obj.fin
        lista_obj.fin.ant = objetivo.ant

    lista_obj.tamanio -= 1
    return dato


def main():
    simple = lista()
    doble = listaDoble()

    for numero in (10, 20, 30, 40, 50):
        insertar(simple, numero)
        insertar_doble(doble, numero)

    print("Lista simplemente enlazada antes:")
    barrido(simple)
    print("Anteúltimo eliminado:", eliminar_anteultimo_simple(simple))
    print("Después:")
    barrido(simple)

    print("\nLista doblemente enlazada antes:")
    barrido_doble(doble)
    print("Anteúltimo eliminado:", eliminar_anteultimo_doble(doble))
    print("Después:")
    barrido_doble(doble)


if __name__ == "__main__":
    main()
