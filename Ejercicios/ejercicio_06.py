"""
Ejercicio 6 - Lista de superhéroes.

Bibliografía:
Walter Bel (2020), Algoritmos y estructuras de datos en Python.
Capítulo VIII - Guía de ejercicios prácticos, pág. 112.
"""

from tda_lista import lista, insertar, buscar, eliminar


class Superheroe:
    def __init__(self, nombre, anio_aparicion, casa, biografia):
        self.nombre = nombre
        self.anio_aparicion = anio_aparicion
        self.casa = casa
        self.biografia = biografia

    def __str__(self):
        return (f"{self.nombre} | {self.anio_aparicion} | "
                f"{self.casa} | {self.biografia}")


def cargar_superheroes():
    superheroes = lista()

    datos = (
        Superheroe("Batman", 1939, "DC", "Utiliza un traje y diferentes dispositivos."),
        Superheroe("Capitana Marvel", 1968, "Marvel", "Heroína con grandes poderes cósmicos."),
        Superheroe("Dr. Strange", 1963, "DC", "Hechicero supremo y protector de la realidad."),
        Superheroe("Flash", 1940, "DC", "Velocista que utiliza un traje especial."),
        Superheroe("Linterna Verde", 1940, "DC", "Portador de un anillo de poder."),
        Superheroe("Mujer Maravilla", 1941, "DC", "Guerrera amazona."),
        Superheroe("Spider-Man", 1962, "Marvel", "Héroe con traje inspirado en una araña."),
        Superheroe("Star-Lord", 1976, "Marvel", "Líder de los Guardianes de la Galaxia."),
        Superheroe("Superman", 1938, "DC", "Kryptoniano con uniforme característico."),
        Superheroe("Wolverine", 1974, "Marvel", "Mutante con esqueleto de adamantium."),
        Superheroe("Iron Man", 1963, "Marvel", "Combate utilizando una armadura tecnológica."),
    )

    for heroe in datos:
        insertar(superheroes, heroe, "nombre")

    return superheroes


def main():
    superheroes = cargar_superheroes()

    # a. eliminar Linterna Verde
    eliminado = eliminar(superheroes, "Linterna Verde", "nombre")
    print("a) Eliminado:", eliminado if eliminado is not None else "No encontrado")

    # b. año de aparición de Wolverine
    pos = buscar(superheroes, "Wolverine", "nombre")
    if pos is not None:
        print("b) Año de aparición de Wolverine:", pos.info.anio_aparicion)

    # c. cambiar la casa de Dr. Strange a Marvel
    pos = buscar(superheroes, "Dr. Strange", "nombre")
    if pos is not None:
        pos.info.casa = "Marvel"
        print("c) Casa de Dr. Strange:", pos.info.casa)

    # d. biografía con "traje" o "armadura"
    print("d) Superhéroes cuya biografía menciona traje o armadura:")
    aux = superheroes.inicio
    while aux is not None:
        bio = aux.info.biografia.lower()
        if "traje" in bio or "armadura" in bio:
            print("  ", aux.info.nombre)
        aux = aux.sig

    # e. fecha de aparición anterior a 1963
    print("e) Superhéroes anteriores a 1963:")
    aux = superheroes.inicio
    while aux is not None:
        if aux.info.anio_aparicion < 1963:
            print(f"   {aux.info.nombre} - {aux.info.casa}")
        aux = aux.sig

    # f. casa de Capitana Marvel y Mujer Maravilla
    print("f) Casas:")
    for nombre in ("Capitana Marvel", "Mujer Maravilla"):
        pos = buscar(superheroes, nombre, "nombre")
        if pos is not None:
            print(f"   {nombre}: {pos.info.casa}")

    # g. toda la información de Flash y Star-Lord
    print("g) Información:")
    for nombre in ("Flash", "Star-Lord"):
        pos = buscar(superheroes, nombre, "nombre")
        if pos is not None:
            print("  ", pos.info)

    # h. comienzan con B, M y S
    print("h) Superhéroes que comienzan con B, M o S:")
    aux = superheroes.inicio
    while aux is not None:
        if aux.info.nombre[0].upper() in ("B", "M", "S"):
            print("  ", aux.info.nombre)
        aux = aux.sig

    # i. cantidad por casa
    marvel = 0
    dc = 0
    aux = superheroes.inicio
    while aux is not None:
        if aux.info.casa == "Marvel":
            marvel += 1
        elif aux.info.casa == "DC":
            dc += 1
        aux = aux.sig

    print("i) Cantidad por casa:")
    print("   Marvel:", marvel)
    print("   DC:", dc)


if __name__ == "__main__":
    main()
