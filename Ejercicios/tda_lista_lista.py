"""
TDA Lista de Lista.
Basado en la modificación explicada al final del capítulo VIII:
cada nodo de la lista principal incorpora una sublista.
"""


def criterio(dato, campo=None):
    dic = {}
    if hasattr(dato, "__dict__"):
        dic = dato.__dict__
    if campo is None or campo not in dic:
        return dato
    return dic[campo]


class nodoListaLista(object):
    def __init__(self, info=None):
        self.info = info
        self.sig = None
        self.sublista = Lista()


class Lista(object):
    def __init__(self):
        self.inicio = None
        self.tamanio = 0


def insertar(lista_obj, dato, campo=None):
    nodo = nodoListaLista(dato)

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


def buscar(lista_obj, buscado, campo=None):
    aux = lista_obj.inicio

    while (aux is not None and
           criterio(aux.info, campo) != criterio(buscado, campo)):
        aux = aux.sig

    return aux


def eliminar(lista_obj, clave, campo=None):
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


def tamanio(lista_obj):
    return lista_obj.tamanio


def barrido(lista_obj):
    aux = lista_obj.inicio
    while aux is not None:
        print(aux.info)
        aux = aux.sig
