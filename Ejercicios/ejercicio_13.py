"""
Ejercicio 13 - Barrido ascendente y descendente con lista doble.

Bibliografía:
Walter Bel (2020), Algoritmos y estructuras de datos en Python.
Capítulo VIII - Guía de ejercicios prácticos, pág. 114.
"""

from tda_lista_doble import listaDoble, insertar, barrido, barrido_inverso


def main():
    numeros = listaDoble()

    for valor in (35, 8, 21, 50, 13, 2, 41):
        insertar(numeros, valor)

    print("Contenido ascendente:")
    barrido(numeros)

    print("\nContenido descendente:")
    barrido_inverso(numeros)


if __name__ == "__main__":
    main()
