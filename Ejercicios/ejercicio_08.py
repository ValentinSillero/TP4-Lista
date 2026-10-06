"""
Ejercicio 8 - Palíndromo con lista doblemente enlazada.

Bibliografía:
Walter Bel (2020), Algoritmos y estructuras de datos en Python.
Capítulo VIII - Guía de ejercicios prácticos, pág. 113.
"""

from tda_lista_doble import listaDoble, insertar_final


def es_palindromo(lista_obj):
    """Compara desde ambos extremos sin usar otra estructura auxiliar."""
    izquierda = lista_obj.inicio
    derecha = lista_obj.fin

    for _ in range(lista_obj.tamanio // 2):
        if izquierda.info != derecha.info:
            return False
        izquierda = izquierda.sig
        derecha = derecha.ant

    return True


def main():
    palabra = input(
        "Ingrese una palabra (Enter para usar 'reconocer'): "
    ).strip().lower()

    if palabra == "":
        palabra = "reconocer"

    caracteres = listaDoble()

    for caracter in palabra:
        insertar_final(caracteres, caracter)

    print("Palabra:", palabra)
    if es_palindromo(caracteres):
        print("Es palíndromo.")
    else:
        print("No es palíndromo.")


if __name__ == "__main__":
    main()
