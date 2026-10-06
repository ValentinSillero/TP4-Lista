"""
TDA Lista simplemente enlazada.

Metodología basada en:
Walter Bel (2020), Algoritmos y estructuras de datos en Python:
un enfoque ágil y estructurado. Capítulo VIII.

Se conserva la idea del libro:
- nodo con info y sig
- lista con inicio y tamanio
- criterio(dato, campo)
- insertar, eliminar, buscar, lista_vacia, tamanio y barrido

Se agregan insertar_final e insertar_descendente solamente como
operaciones auxiliares necesarias para algunos ejercicios de la guía.
"""


class nodoLista(object):
    def __init__(self, info=None):
        self.info = info
        self.sig = None


class lista(object):
    def __init__(self):
        self.inicio = None
        self.tamanio = 0


def criterio(dato, campo=None):
    """Determina el campo por el cual se comparará el dato."""
    dic = {}
    if hasattr(dato, "__dict__"):
        dic = dato.__dict__

    if campo is None or campo not in dic:
        return dato
    return dic[campo]


def insertar(lista_obj, dato, campo=None):
    """Inserta un dato manteniendo la lista ordenada de forma ascendente."""
    nodo = nodoLista(dato)

    if (lista_obj.inicio is None or
            criterio(lista_obj.inicio.info, campo) > criterio(dato, campo)):
        nodo.sig = lista_obj.inicio
        lista_obj.inicio = nodo
    else:
        ant = lista_obj.inicio
        act = lista_obj.inicio.sig

        while (act is not None and
               criterio(act.info, campo) < criterio(dato, campo)):
            ant = ant.sig
            act = act.sig

        nodo.sig = act
        ant.sig = nodo

    lista_obj.tamanio += 1


def insertar_final(lista_obj, dato):
    """Agrega un dato al final. Extensión auxiliar para conservar un orden dado."""
    nodo = nodoLista(dato)

    if lista_obj.inicio is None:
        lista_obj.inicio = nodo
    else:
        aux = lista_obj.inicio
        while aux.sig is not None:
            aux = aux.sig
        aux.sig = nodo

    lista_obj.tamanio += 1


def insertar_descendente(lista_obj, dato, campo=None):
    """Inserta un dato manteniendo orden descendente. Extensión auxiliar."""
    nodo = nodoLista(dato)

    if (lista_obj.inicio is None or
            criterio(lista_obj.inicio.info, campo) < criterio(dato, campo)):
        nodo.sig = lista_obj.inicio
        lista_obj.inicio = nodo
    else:
        ant = lista_obj.inicio
        act = lista_obj.inicio.sig

        while (act is not None and
               criterio(act.info, campo) > criterio(dato, campo)):
            ant = ant.sig
            act = act.sig

        nodo.sig = act
        ant.sig = nodo

    lista_obj.tamanio += 1


def lista_vacia(lista_obj):
    return lista_obj.inicio is None


def eliminar(lista_obj, clave, campo=None):
    """Elimina el primer elemento que coincide con la clave y lo devuelve."""
    dato = None

    if lista_obj.inicio is None:
        return dato

    if criterio(lista_obj.inicio.info, campo) == criterio(clave, campo):
        dato = lista_obj.inicio.info
        lista_obj.inicio = lista_obj.inicio.sig
        lista_obj.tamanio -= 1
    else:
        anterior = lista_obj.inicio
        actual = lista_obj.inicio.sig

        while (actual is not None and
               criterio(actual.info, campo) != criterio(clave, campo)):
            anterior = anterior.sig
            actual = actual.sig

        if actual is not None:
            dato = actual.info
            anterior.sig = actual.sig
            lista_obj.tamanio -= 1

    return dato


def buscar(lista_obj, buscado, campo=None):
    """Devuelve el nodo que contiene el elemento buscado o None."""
    aux = lista_obj.inicio

    while (aux is not None and
           criterio(aux.info, campo) != criterio(buscado, campo)):
        aux = aux.sig

    return aux


def tamanio(lista_obj):
    return lista_obj.tamanio


def barrido(lista_obj):
    aux = lista_obj.inicio
    while aux is not None:
        print(aux.info)
        aux = aux.sig
