"""
Ejercicio 9 - Alumnos y parciales con Lista de Lista.

Bibliografía:
Walter Bel (2020), Algoritmos y estructuras de datos en Python.
Capítulo VIII - Lista de lista y guía de ejercicios, págs. 110-113.

NOTA:
El enunciado no fija la nota mínima de aprobación. Se deja parametrizada
en NOTA_APROBACION = 6 para que pueda modificarse fácilmente si la
cátedra utiliza otro criterio.
"""

from tda_lista_lista import Lista, insertar, buscar

NOTA_APROBACION = 6


class Alumno:
    def __init__(self, nombre, apellido, legajo):
        self.nombre = nombre
        self.apellido = apellido
        self.legajo = legajo

    def __str__(self):
        return f"{self.apellido}, {self.nombre} - Legajo {self.legajo}"


class Parcial:
    def __init__(self, materia, nota, fecha):
        self.materia = materia
        self.nota = nota
        self.fecha = fecha

    def __str__(self):
        return f"{self.materia} | Nota: {self.nota} | Fecha: {self.fecha}"


def agregar_alumno(alumnos, alumno):
    insertar(alumnos, alumno, "apellido")


def agregar_parcial(alumnos, legajo, parcial):
    alumno_nodo = buscar(alumnos, legajo, "legajo")
    if alumno_nodo is not None:
        insertar(alumno_nodo.sublista, parcial, "fecha")


def promedio(parciales):
    if parciales.tamanio == 0:
        return 0

    suma = 0
    aux = parciales.inicio
    while aux is not None:
        suma += aux.info.nota
        aux = aux.sig

    return suma / parciales.tamanio


def no_desaprobo_ninguno(parciales):
    if parciales.inicio is None:
        return False

    aux = parciales.inicio
    while aux is not None:
        if aux.info.nota < NOTA_APROBACION:
            return False
        aux = aux.sig

    return True


def rindio_materia(parciales, materia):
    aux = parciales.inicio
    while aux is not None:
        if aux.info.materia.lower() == materia.lower():
            return True
        aux = aux.sig
    return False


def porcentaje_aprobados(parciales):
    if parciales.tamanio == 0:
        return 0

    aprobados = 0
    aux = parciales.inicio

    while aux is not None:
        if aux.info.nota >= NOTA_APROBACION:
            aprobados += 1
        aux = aux.sig

    return aprobados * 100 / parciales.tamanio


def mostrar_alumno_y_parciales(nodo):
    print(nodo.info)
    aux = nodo.sublista.inicio
    while aux is not None:
        print("   ", aux.info)
        aux = aux.sig


def cargar_datos():
    alumnos = Lista()

    for alumno in (
        Alumno("Ana", "Lopez", 1001),
        Alumno("Bruno", "Martinez", 1002),
        Alumno("Carla", "Luna", 1003),
        Alumno("Diego", "Perez", 1004),
        Alumno("Elena", "Suarez", 1005),
    ):
        agregar_alumno(alumnos, alumno)

    parciales = (
        (1001, Parcial("Algoritmos y estructuras de datos", 10, "2020-05-15")),
        (1001, Parcial("Base de datos", 9, "2020-08-20")),
        (1001, Parcial("Programacion", 9, "2021-04-10")),

        (1002, Parcial("Algoritmos y estructuras de datos", 8, "2020-05-15")),
        (1002, Parcial("Base de datos", 5, "2020-08-20")),
        (1002, Parcial("Programacion", 7, "2021-04-10")),

        (1003, Parcial("Algoritmos y estructuras de datos", 9, "2020-05-15")),
        (1003, Parcial("Base de datos", 10, "2021-08-20")),
        (1003, Parcial("Programacion", 9, "2021-04-10")),

        (1004, Parcial("Base de datos", 4, "2019-08-20")),
        (1004, Parcial("Programacion", 6, "2019-11-12")),

        (1005, Parcial("Algoritmos y estructuras de datos", 7, "2022-05-15")),
        (1005, Parcial("Base de datos", 8, "2022-08-20")),
    )

    for legajo, parcial in parciales:
        agregar_parcial(alumnos, legajo, parcial)

    return alumnos


def main():
    alumnos = cargar_datos()

    # a
    print("a) Alumnos ordenados alfabéticamente por apellido:")
    aux = alumnos.inicio
    while aux is not None:
        print("  ", aux.info)
        aux = aux.sig

    # b
    print("\nb) Alumnos que no desaprobaron ningún parcial:")
    aux = alumnos.inicio
    while aux is not None:
        if no_desaprobo_ninguno(aux.sublista):
            print("  ", aux.info)
        aux = aux.sig

    # c
    print("\nc) Alumnos con promedio mayor a 8,89:")
    aux = alumnos.inicio
    while aux is not None:
        prom = promedio(aux.sublista)
        if prom > 8.89:
            print(f"   {aux.info} - Promedio: {prom:.2f}")
        aux = aux.sig

    # d
    print("\nd) Información de alumnos cuyo apellido comienza con L:")
    aux = alumnos.inicio
    while aux is not None:
        if aux.info.apellido.upper().startswith("L"):
            mostrar_alumno_y_parciales(aux)
        aux = aux.sig

    # e
    print("\ne) Promedio de cada alumno:")
    aux = alumnos.inicio
    while aux is not None:
        print(f"   {aux.info}: {promedio(aux.sublista):.2f}")
        aux = aux.sig

    # f
    print("\nf) Alumnos que rindieron Algoritmos y estructuras de datos:")
    aux = alumnos.inicio
    while aux is not None:
        if rindio_materia(aux.sublista, "Algoritmos y estructuras de datos"):
            print("  ", aux.info)
        aux = aux.sig

    # g
    entrada = input(
        "\ng) Ingrese legajo para calcular porcentaje de parciales aprobados "
        "(Enter = 1001): "
    ).strip()
    legajo = 1001 if entrada == "" else int(entrada)

    alumno = buscar(alumnos, legajo, "legajo")
    if alumno is not None:
        print(f"   {alumno.info}: {porcentaje_aprobados(alumno.sublista):.2f}%")
    else:
        print("   Alumno no encontrado.")

    # h
    aprobados_bd = 0
    desaprobados_bd = 0
    aux = alumnos.inicio
    while aux is not None:
        parcial = aux.sublista.inicio
        while parcial is not None:
            if parcial.info.materia.lower() == "base de datos":
                if parcial.info.nota >= NOTA_APROBACION:
                    aprobados_bd += 1
                else:
                    desaprobados_bd += 1
            parcial = parcial.sig
        aux = aux.sig

    print("\nh) Base de datos:")
    print("   Aprobados:", aprobados_bd)
    print("   Desaprobados:", desaprobados_bd)

    # i
    print("\ni) Alumnos que rindieron en el año 2020:")
    aux = alumnos.inicio
    while aux is not None:
        rindio_2020 = False
        parcial = aux.sublista.inicio
        while parcial is not None:
            if parcial.info.fecha.startswith("2020"):
                rindio_2020 = True
                break
            parcial = parcial.sig

        if rindio_2020:
            print("  ", aux.info)
        aux = aux.sig

    # j se cumple utilizando el TDA Lista de Lista.


if __name__ == "__main__":
    main()
