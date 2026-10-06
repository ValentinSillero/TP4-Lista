"""
Ejercicio 14 - Juego de dados con lista circular.

Bibliografía:
Walter Bel (2020), Algoritmos y estructuras de datos en Python.
Capítulo VIII - Guía de ejercicios prácticos, pág. 114.
"""

from random import randint, seed
from tda_lista_circular import listaCircular, insertar, barrido


class Jugador:
    def __init__(self, numero, nombre):
        self.numero = numero
        self.nombre = nombre

    def __str__(self):
        return f"{self.numero} - {self.nombre}"


def cargar_jugadores():
    jugadores = listaCircular()
    nombres = ("Ana", "Bruno", "Carla", "Diego", "Elena")
    usados = set()

    for nombre in nombres:
        numero = randint(1, 100)
        while numero in usados:
            numero = randint(1, 100)

        usados.add(numero)
        insertar(jugadores, Jugador(numero, nombre), "numero")

    return jugadores


def jugar(jugadores):
    if jugadores.inicio is None:
        return None

    actual = jugadores.inicio
    turno = 1

    while True:
        dado = randint(1, 6)
        print(f"Turno {turno}: {actual.info.nombre} sacó {dado}")

        if dado == 5:
            return actual.info

        # Al ser circular, después del último nodo se vuelve al primero.
        actual = actual.sig
        turno += 1


def main():
    # Semilla para que la demostración sea reproducible.
    # Puede comentarse para que cada ejecución sea completamente distinta.
    seed(14)

    jugadores = cargar_jugadores()

    print("Jugadores según el orden de la lista circular:")
    barrido(jugadores)

    print("\nComienza el juego:")
    ganador = jugar(jugadores)
    print("\nGanador:", ganador.nombre)


if __name__ == "__main__":
    main()
