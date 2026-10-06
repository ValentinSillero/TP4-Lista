"""
Ejercicio 7 - Operaciones entre listas.

Bibliografía:
Walter Bel (2020), Algoritmos y estructuras de datos en Python.
Capítulo VIII - Guía de ejercicios prácticos, págs. 112-113.
"""

from tda_lista import (
    lista, insertar, insertar_final, buscar, eliminar, lista_vacia, barrido
)


def concatenar(lista1, lista2):
    """Concatena una lista detrás de la otra conservando el orden de ambas."""
    resultado = lista()

    aux = lista1.inicio
    while aux is not None:
        insertar_final(resultado, aux.info)
        aux = aux.sig

    aux = lista2.inicio
    while aux is not None:
        insertar_final(resultado, aux.info)
        aux = aux.sig

    return resultado


def concatenar_sin_repetidos(lista1, lista2):
    """Concatena sin repetir datos y conserva el orden de primera aparición."""
    resultado = lista()

    aux = lista1.inicio
    while aux is not None:
        if buscar(resultado, aux.info) is None:
            insertar_final(resultado, aux.info)
        aux = aux.sig

    aux = lista2.inicio
    while aux is not None:
        if buscar(resultado, aux.info) is None:
            insertar_final(resultado, aux.info)
        aux = aux.sig

    return resultado


def cantidad_repetidos(lista1, lista2):
    """Cuenta la intersección entre ambas listas."""
    cantidad = 0
    aux = lista1.inicio

    while aux is not None:
        if buscar(lista2, aux.info) is not None:
            cantidad += 1
        aux = aux.sig

    return cantidad


def eliminar_todos(lista_obj):
    """Elimina los nodos de a uno mostrando el contenido eliminado."""
    while not lista_vacia(lista_obj):
        clave = lista_obj.inicio.info
        dato = eliminar(lista_obj, clave)
        print("  Eliminado:", dato)


def main():
    lista1 = lista()
    lista2 = lista()

    for dato in (1, 3, 5, 7, 9):
        insertar(lista1, dato)

    for dato in (2, 3, 5, 8, 9):
        insertar(lista2, dato)

    print("Lista 1:")
    barrido(lista1)
    print("Lista 2:")
    barrido(lista2)

    print("\na) Concatenadas, una detrás de la otra:")
    concatenada = concatenar(lista1, lista2)
    barrido(concatenada)

    print("\nb) Concatenadas sin repetidos:")
    sin_repetidos = concatenar_sin_repetidos(lista1, lista2)
    barrido(sin_repetidos)

    print("\nc) Cantidad de elementos repetidos:",
          cantidad_repetidos(lista1, lista2))

    print("\nd) Eliminación de todos los nodos de la lista concatenada:")
    eliminar_todos(concatenada)


if __name__ == "__main__":
    main()
