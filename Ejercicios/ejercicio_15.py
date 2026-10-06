"""
Ejercicio 15 - Entrenadores Pokémon con Lista de Lista.

Bibliografía:
Walter Bel (2020), Algoritmos y estructuras de datos en Python.
Capítulo VIII - Guía de ejercicios prácticos, págs. 114-115.
"""

from tda_lista_lista import Lista, insertar, buscar


class Entrenador:
    def __init__(self, nombre, torneos_ganados, batallas_perdidas, batallas_ganadas):
        self.nombre = nombre
        self.torneos_ganados = torneos_ganados
        self.batallas_perdidas = batallas_perdidas
        self.batallas_ganadas = batallas_ganadas

    def __str__(self):
        return (f"{self.nombre} | torneos={self.torneos_ganados} | "
                f"ganadas={self.batallas_ganadas} | "
                f"perdidas={self.batallas_perdidas}")


class Pokemon:
    def __init__(self, nombre, nivel, tipo, subtipo):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        return (f"{self.nombre} | nivel={self.nivel} | "
                f"tipo={self.tipo} | subtipo={self.subtipo}")


def agregar_entrenador(entrenadores, entrenador):
    insertar(entrenadores, entrenador, "nombre")


def agregar_pokemon(entrenadores, entrenador_nombre, pokemon):
    entrenador = buscar(entrenadores, entrenador_nombre, "nombre")
    if entrenador is not None:
        insertar(entrenador.sublista, pokemon, "nombre")


def cargar_datos():
    entrenadores = Lista()

    for entrenador in (
        Entrenador("Ash", 5, 20, 95),
        Entrenador("Brock", 4, 30, 70),
        Entrenador("Iris", 6, 10, 90),
        Entrenador("Misty", 2, 15, 80),
    ):
        agregar_entrenador(entrenadores, entrenador)

    datos_pokemon = (
        ("Ash", Pokemon("Pikachu", 85, "Electrico", "Ninguno")),
        ("Ash", Pokemon("Pikachu", 72, "Electrico", "Ninguno")),
        ("Ash", Pokemon("Charizard", 82, "Fuego", "Volador")),
        ("Ash", Pokemon("Wingull", 42, "Agua", "Volador")),

        ("Brock", Pokemon("Onix", 70, "Roca", "Tierra")),
        ("Brock", Pokemon("Tyrantrum", 78, "Roca", "Dragon")),
        ("Brock", Pokemon("Terrakion", 84, "Roca", "Lucha")),

        ("Iris", Pokemon("Haxorus", 91, "Dragon", "Ninguno")),
        ("Iris", Pokemon("Scovillain", 76, "Fuego", "Planta")),
        ("Iris", Pokemon("Dragonite", 88, "Dragon", "Volador")),

        ("Misty", Pokemon("Starmie", 73, "Agua", "Psiquico")),
        ("Misty", Pokemon("Wingull", 55, "Agua", "Volador")),
        ("Misty", Pokemon("Psyduck", 50, "Agua", "Ninguno")),
    )

    for entrenador, pokemon in datos_pokemon:
        agregar_pokemon(entrenadores, entrenador, pokemon)

    return entrenadores


def porcentaje_batallas_ganadas(entrenador):
    total = entrenador.batallas_ganadas + entrenador.batallas_perdidas
    if total == 0:
        return 0
    return entrenador.batallas_ganadas * 100 / total


def pokemon_mayor_nivel(pokemons):
    mayor = None
    aux = pokemons.inicio

    while aux is not None:
        if mayor is None or aux.info.nivel > mayor.nivel:
            mayor = aux.info
        aux = aux.sig

    return mayor


def mostrar_entrenador_con_pokemons(nodo):
    print(nodo.info)
    aux = nodo.sublista.inicio
    while aux is not None:
        print("   ", aux.info)
        aux = aux.sig


def tiene_combinacion_tipo(pokemons):
    aux = pokemons.inicio

    while aux is not None:
        tipo = aux.info.tipo.lower()
        subtipo = aux.info.subtipo.lower()

        fuego_planta = (
            (tipo == "fuego" and subtipo == "planta") or
            (tipo == "planta" and subtipo == "fuego")
        )
        agua_volador = (
            (tipo == "agua" and subtipo == "volador") or
            (tipo == "volador" and subtipo == "agua")
        )

        if fuego_planta or agua_volador:
            return True

        aux = aux.sig

    return False


def promedio_nivel(pokemons):
    if pokemons.tamanio == 0:
        return 0

    suma = 0
    aux = pokemons.inicio

    while aux is not None:
        suma += aux.info.nivel
        aux = aux.sig

    return suma / pokemons.tamanio


def tiene_repetidos(pokemons):
    aux = pokemons.inicio

    while aux is not None:
        otro = aux.sig
        while otro is not None:
            if aux.info.nombre == otro.info.nombre:
                return True
            otro = otro.sig
        aux = aux.sig

    return False


def tiene_alguno(pokemons, nombres):
    aux = pokemons.inicio
    while aux is not None:
        if aux.info.nombre in nombres:
            return True
        aux = aux.sig
    return False


def main():
    entrenadores = cargar_datos()

    # a
    entrada = input(
        "a) Entrenador para contar sus Pokémon (Enter = Ash): "
    ).strip()
    nombre_entrenador = "Ash" if entrada == "" else entrada

    entrenador = buscar(entrenadores, nombre_entrenador, "nombre")
    if entrenador is not None:
        print(f"   {entrenador.info.nombre} tiene "
              f"{entrenador.sublista.tamanio} Pokémon.")
    else:
        print("   Entrenador no encontrado.")

    # b
    print("\nb) Entrenadores con más de tres torneos ganados:")
    aux = entrenadores.inicio
    while aux is not None:
        if aux.info.torneos_ganados > 3:
            print("  ", aux.info.nombre)
        aux = aux.sig

    # c
    entrenador_mas_torneos = None
    aux = entrenadores.inicio
    while aux is not None:
        if (entrenador_mas_torneos is None or
                aux.info.torneos_ganados >
                entrenador_mas_torneos.info.torneos_ganados):
            entrenador_mas_torneos = aux
        aux = aux.sig

    print("\nc) Pokémon de mayor nivel del entrenador con más torneos:")
    if entrenador_mas_torneos is not None:
        mayor = pokemon_mayor_nivel(entrenador_mas_torneos.sublista)
        print("   Entrenador:", entrenador_mas_torneos.info.nombre)
        print("   Pokémon:", mayor)

    # d
    print("\nd) Todos los entrenadores y sus Pokémon:")
    aux = entrenadores.inicio
    while aux is not None:
        mostrar_entrenador_con_pokemons(aux)
        aux = aux.sig

    # e
    print("\ne) Entrenadores con porcentaje de victorias mayor al 79%:")
    aux = entrenadores.inicio
    while aux is not None:
        porcentaje = porcentaje_batallas_ganadas(aux.info)
        if porcentaje > 79:
            print(f"   {aux.info.nombre}: {porcentaje:.2f}%")
        aux = aux.sig

    # f
    print("\nf) Entrenadores con Pokémon fuego/planta o agua/volador:")
    aux = entrenadores.inicio
    while aux is not None:
        if tiene_combinacion_tipo(aux.sublista):
            print("  ", aux.info.nombre)
        aux = aux.sig

    # g
    entrada = input(
        "\ng) Entrenador para promedio de nivel (Enter = Misty): "
    ).strip()
    nombre_promedio = "Misty" if entrada == "" else entrada

    entrenador = buscar(entrenadores, nombre_promedio, "nombre")
    if entrenador is not None:
        print(f"   Promedio de nivel de {entrenador.info.nombre}: "
              f"{promedio_nivel(entrenador.sublista):.2f}")
    else:
        print("   Entrenador no encontrado.")

    # h
    entrada = input(
        "\nh) Pokémon para contar entrenadores que lo tienen "
        "(Enter = Wingull): "
    ).strip()
    pokemon_buscado = "Wingull" if entrada == "" else entrada

    cantidad = 0
    aux = entrenadores.inicio
    while aux is not None:
        if buscar(aux.sublista, pokemon_buscado, "nombre") is not None:
            cantidad += 1
        aux = aux.sig

    print(f"   {cantidad} entrenador(es) tienen a {pokemon_buscado}.")

    # i
    print("\ni) Entrenadores con Pokémon repetidos:")
    aux = entrenadores.inicio
    while aux is not None:
        if tiene_repetidos(aux.sublista):
            print("  ", aux.info.nombre)
        aux = aux.sig

    # j
    print("\nj) Entrenadores con Tyrantrum, Terrakion o Wingull:")
    buscados = ("Tyrantrum", "Terrakion", "Wingull")
    aux = entrenadores.inicio
    while aux is not None:
        if tiene_alguno(aux.sublista, buscados):
            print("  ", aux.info.nombre)
        aux = aux.sig

    # k
    entrada_entrenador = input(
        "\nk) Nombre del entrenador X (Enter = Brock): "
    ).strip()
    entrada_pokemon = input(
        "   Nombre del Pokémon Y (Enter = Tyrantrum): "
    ).strip()

    x = "Brock" if entrada_entrenador == "" else entrada_entrenador
    y = "Tyrantrum" if entrada_pokemon == "" else entrada_pokemon

    entrenador = buscar(entrenadores, x, "nombre")
    if entrenador is None:
        print("   Entrenador no encontrado.")
    else:
        pokemon = buscar(entrenador.sublista, y, "nombre")
        if pokemon is None:
            print(f"   {x} no tiene a {y}.")
        else:
            print("   Entrenador:", entrenador.info)
            print("   Pokémon:", pokemon.info)


if __name__ == "__main__":
    main()
