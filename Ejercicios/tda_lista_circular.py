"""
TDA Lista circular simplemente enlazada.
Extensión del TDA Lista del capítulo VIII de Walter Bel (2020).
"""


def criterio(dato, campo=None):
    dic = {}
    if hasattr(dato, "__dict__"):
        dic = dato.__dict__
    if campo is None or campo not in dic:
        return dato
    return dic[campo]


class nodoListaCircular(object):
    def __init__(self, info=None):
        self.info = info
        self.sig = None


class listaCircular(object):
    def __init__(self):
        self.inicio = None
        self.tamanio = 0


def insertar(lista_obj, dato, campo=None):
    """Inserción ordenada ascendente en una lista circular."""
    nodo = nodoListaCircular(dato)

    if lista_obj.inicio is None:
        nodo.sig = nodo
        lista_obj.inicio = nodo
    elif criterio(dato, campo) < criterio(lista_obj.inicio.info, campo):
        ultimo = lista_obj.inicio
        while ultimo.sig != lista_obj.inicio:
            ultimo = ultimo.sig

        nodo.sig = lista_obj.inicio
        ultimo.sig = nodo
        lista_obj.inicio = nodo
    else:
        actual = lista_obj.inicio

        while (actual.sig != lista_obj.inicio and
               criterio(actual.sig.info, campo) < criterio(dato, campo)):
            actual = actual.sig

        nodo.sig = actual.sig
        actual.sig = nodo

    lista_obj.tamanio += 1


def barrido(lista_obj):
    if lista_obj.inicio is None:
        return

    aux = lista_obj.inicio
    while True:
        print(aux.info)
        aux = aux.sig
        if aux == lista_obj.inicio:
            break


def tamanio(lista_obj):
    return lista_obj.tamanio
