"""
Ejercicio 11 - Personajes de Star Wars.

Bibliografía:
Walter Bel (2020), Algoritmos y estructuras de datos en Python.
Capítulo VIII - Guía de ejercicios prácticos, págs. 113-114.
"""

from tda_lista import lista, insertar, buscar, eliminar


class Personaje:
    def __init__(self, nombre, altura, edad, genero, especie, planeta, episodios):
        self.nombre = nombre
        self.altura = altura
        self.edad = edad
        self.genero = genero
        self.especie = especie
        self.planeta = planeta
        self.episodios = episodios

    def __str__(self):
        return (f"{self.nombre} | altura={self.altura} cm | edad={self.edad} | "
                f"género={self.genero} | especie={self.especie} | "
                f"planeta={self.planeta} | episodios={self.episodios}")


def cargar_personajes():
    personajes = lista()

    datos = (
        Personaje("Ahsoka Tano", 188, 47, "F", "Togruta", "Shili", (7,)),
        Personaje("Bail Organa", 191, 67, "M", "Humano", "Alderaan", (2, 3, 4)),
        Personaje("C-3PO", 175, 67, "M", "Droide", "Tatooine", (1, 2, 3, 4, 5, 6, 7)),
        Personaje("Chewbacca", 228, 200, "M", "Wookiee", "Kashyyyk", (3, 4, 5, 6, 7)),
        Personaje("Darth Vader", 202, 45, "M", "Humano", "Tatooine", (3, 4, 5, 6)),
        Personaje("Han Solo", 180, 66, "M", "Humano", "Corellia", (4, 5, 6, 7)),
        Personaje("Leia Organa", 150, 54, "F", "Humano", "Alderaan", (3, 4, 5, 6, 7)),
        Personaje("Luke Skywalker", 172, 53, "M", "Humano", "Tatooine", (3, 4, 5, 6, 7)),
        Personaje("Maz Kanata", 124, 1000, "F", "Desconocida", "Takodana", (7,)),
        Personaje("R2-D2", 96, 66, "M", "Droide", "Naboo", (1, 2, 3, 4, 5, 6, 7)),
        Personaje("Yoda", 66, 900, "M", "Desconocida", "Desconocido", (1, 2, 3, 5, 6)),
        Personaje("Wicket", 60, 30, "M", "Ewok", "Endor", (6,)),
        Personaje("Mon Mothma", 150, 70, "F", "Humano", "Chandrila", (3, 6)),
    )

    for personaje in datos:
        insertar(personajes, personaje, "nombre")

    return personajes


def contiene_todos(episodios, requeridos):
    for episodio in requeridos:
        if episodio not in episodios:
            return False
    return True


def solo_trilogia_clasica(episodios):
    if len(episodios) == 0:
        return False

    for episodio in episodios:
        if episodio not in (4, 5, 6):
            return False

    return True


def main():
    personajes = cargar_personajes()

    # a
    print("a) Personajes de género femenino:")
    aux = personajes.inicio
    while aux is not None:
        if aux.info.genero == "F":
            print("  ", aux.info.nombre)
        aux = aux.sig

    # b
    print("\nb) Droides que aparecieron en los primeros seis episodios:")
    aux = personajes.inicio
    while aux is not None:
        if (aux.info.especie == "Droide" and
                contiene_todos(aux.info.episodios, (1, 2, 3, 4, 5, 6))):
            print("  ", aux.info.nombre)
        aux = aux.sig

    # c
    print("\nc) Darth Vader y Han Solo:")
    for nombre in ("Darth Vader", "Han Solo"):
        pos = buscar(personajes, nombre, "nombre")
        if pos is not None:
            print("  ", pos.info)

    # d
    print("\nd) Personajes que aparecen en VII y en los tres anteriores:")
    aux = personajes.inicio
    while aux is not None:
        if contiene_todos(aux.info.episodios, (4, 5, 6, 7)):
            print("  ", aux.info.nombre)
        aux = aux.sig

    # e
    print("\ne) Personajes mayores a 850 años:")
    mayor = None
    aux = personajes.inicio
    while aux is not None:
        if aux.info.edad > 850:
            print("  ", aux.info.nombre, "-", aux.info.edad)
            if mayor is None or aux.info.edad > mayor.edad:
                mayor = aux.info
        aux = aux.sig

    if mayor is not None:
        print("   El mayor es:", mayor.nombre, "-", mayor.edad)

    # f
    print("\nf) Eliminando personajes que solamente aparecieron en IV, V y VI:")
    aux = personajes.inicio
    while aux is not None:
        siguiente = aux.sig
        if solo_trilogia_clasica(aux.info.episodios):
            eliminado = eliminar(personajes, aux.info.nombre, "nombre")
            print("   Eliminado:", eliminado.nombre)
        aux = siguiente

    # g
    print("\ng) Humanos cuyo planeta de origen es Alderaan:")
    aux = personajes.inicio
    while aux is not None:
        if aux.info.especie == "Humano" and aux.info.planeta == "Alderaan":
            print("  ", aux.info.nombre)
        aux = aux.sig

    # h
    print("\nh) Personajes con altura menor a 70 cm:")
    aux = personajes.inicio
    while aux is not None:
        if aux.info.altura < 70:
            print("  ", aux.info)
        aux = aux.sig

    # i
    print("\ni) Chewbacca:")
    pos = buscar(personajes, "Chewbacca", "nombre")
    if pos is not None:
        print("   Episodios:", pos.info.episodios)
        print("   Información:", pos.info)


if __name__ == "__main__":
    main()
