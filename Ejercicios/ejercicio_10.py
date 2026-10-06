"""
Ejercicio 10 - Canciones de Spotify.

Bibliografía:
Walter Bel (2020), Algoritmos y estructuras de datos en Python.
Capítulo VIII - Guía de ejercicios prácticos, pág. 113.
"""

from tda_lista import lista, insertar, insertar_descendente


class Cancion:
    def __init__(self, nombre, artista, duracion, reproducciones):
        self.nombre = nombre
        self.artista = artista
        self.duracion = duracion       # segundos
        self.reproducciones = reproducciones

    def __str__(self):
        minutos = self.duracion // 60
        segundos = self.duracion % 60
        return (f"{self.nombre} - {self.artista} | "
                f"{minutos}:{segundos:02d} | "
                f"{self.reproducciones} reproducciones")


def cargar_canciones():
    canciones = lista()

    especiales = (
        Cancion("Do I Wanna Know?", "Arctic Monkeys", 272, 9500000),
        Cancion("R U Mine?", "Arctic Monkeys", 201, 8200000),
        Cancion("505", "Arctic Monkeys", 253, 11000000),
        Cancion("Fluorescent Adolescent", "Arctic Monkeys", 173, 7600000),
        Cancion("Starlight", "Muse", 240, 8700000),
        Cancion("Hello", "Adele", 295, 9900000),
        Cancion("Bohemian Rhapsody", "Queen", 354, 13000000),
        Cancion("Everlong", "Foo Fighters", 250, 7200000),
    )

    for cancion in especiales:
        insertar(canciones, cancion, "nombre")

    # Datos de prueba adicionales para que el algoritmo pueda mostrar TOP 40.
    for i in range(1, 38):
        artista = "Muse" if i % 7 == 0 else f"Artista {i}"
        cancion = Cancion(
            f"Cancion {i:02d}",
            artista,
            160 + (i * 7) % 210,
            500000 + i * 173421
        )
        insertar(canciones, cancion, "nombre")

    return canciones


def cancion_mas_larga(canciones):
    mayor = canciones.inicio
    aux = canciones.inicio

    while aux is not None:
        if mayor is None or aux.info.duracion > mayor.info.duracion:
            mayor = aux
        aux = aux.sig

    return mayor.info if mayor is not None else None


def ordenar_por_reproducciones_desc(canciones):
    ordenadas = lista()
    aux = canciones.inicio

    while aux is not None:
        insertar_descendente(ordenadas, aux.info, "reproducciones")
        aux = aux.sig

    return ordenadas


def mostrar_top(canciones_ordenadas, cantidad):
    aux = canciones_ordenadas.inicio
    posicion = 1

    while aux is not None and posicion <= cantidad:
        print(f"   {posicion}. {aux.info}")
        posicion += 1
        aux = aux.sig


def main():
    canciones = cargar_canciones()

    # a
    print("a) Canción más larga:")
    print("  ", cancion_mas_larga(canciones))

    # b
    ordenadas = ordenar_por_reproducciones_desc(canciones)

    print("\nb) TOP 5:")
    mostrar_top(ordenadas, 5)

    print("\nTOP 10:")
    mostrar_top(ordenadas, 10)

    print("\nTOP 40:")
    mostrar_top(ordenadas, 40)

    # c
    print("\nc) Canciones de Arctic Monkeys:")
    aux = canciones.inicio
    while aux is not None:
        if aux.info.artista == "Arctic Monkeys":
            print("  ", aux.info)
        aux = aux.sig

    # d
    print("\nd) Bandas o artistas cuyo nombre tiene una sola palabra:")
    mostrados = lista()
    aux = canciones.inicio

    while aux is not None:
        artista = aux.info.artista
        if " " not in artista:
            # Evita repetir el mismo artista en la salida.
            encontrado = mostrados.inicio
            repetido = False
            while encontrado is not None:
                if encontrado.info == artista:
                    repetido = True
                    break
                encontrado = encontrado.sig

            if not repetido:
                insertar(mostrados, artista)
                print("  ", artista)

        aux = aux.sig


if __name__ == "__main__":
    main()
