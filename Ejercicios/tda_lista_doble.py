"""
TDA Lista doblemente enlazada.
Extensión del TDA Lista del capítulo VIII de Walter Bel (2020).
"""


def criterio(dato, campo=None):
    dic = {}
    if hasattr(dato, "__dict__"):
        dic = dato.__dict__
    if campo is None or campo not in dic:
        return dato
    return dic[campo]


class nodoListaDoble(object):
    def __init__(self, info=None):
        self.info = info
        self.ant = None
        self.sig = None


class listaDoble(object):
    def __init__(self):
        self.inicio = None
        self.fin = None
        self.tamanio = 0


def insertar(lista_obj, dato, campo=None):
    """Inserción ordenada ascendente."""
    nodo = nodoListaDoble(dato)

    if lista_obj.inicio is None:
        lista_obj.inicio = nodo
        lista_obj.fin = nodo
    elif criterio(dato, campo) < criterio(lista_obj.inicio.info, campo):
        nodo.sig = lista_obj.inicio
        lista_obj.inicio.ant = nodo
        lista_obj.inicio = nodo
    else:
        actual = lista_obj.inicio

        while (actual.sig is not None and
               criterio(actual.sig.info, campo) < criterio(dato, campo)):
            actual = actual.sig

        nodo.sig = actual.sig
        nodo.ant = actual

        if actual.sig is not None:
            actual.sig.ant = nodo
        else:
            lista_obj.fin = nodo

        actual.sig = nodo

    lista_obj.tamanio += 1


def insertar_final(lista_obj, dato):
    """Inserta al final conservando exactamente el orden de carga."""
    nodo = nodoListaDoble(dato)

    if lista_obj.inicio is None:
        lista_obj.inicio = nodo
        lista_obj.fin = nodo
    else:
        nodo.ant = lista_obj.fin
        lista_obj.fin.sig = nodo
        lista_obj.fin = nodo

    lista_obj.tamanio += 1


def buscar(lista_obj, buscado, campo=None):
    aux = lista_obj.inicio
    while (aux is not None and
           criterio(aux.info, campo) != criterio(buscado, campo)):
        aux = aux.sig
    return aux


def eliminar(lista_obj, clave, campo=None):
    actual = buscar(lista_obj, clave, campo)

    if actual is None:
        return None

    if actual.ant is not None:
        actual.ant.sig = actual.sig
    else:
        lista_obj.inicio = actual.sig

    if actual.sig is not None:
        actual.sig.ant = actual.ant
    else:
        lista_obj.fin = actual.ant

    lista_obj.tamanio -= 1
    return actual.info


def tamanio(lista_obj):
    return lista_obj.tamanio


def barrido(lista_obj):
    aux = lista_obj.inicio
    while aux is not None:
        print(aux.info)
        aux = aux.sig


def barrido_inverso(lista_obj):
    aux = lista_obj.fin
    while aux is not None:
        print(aux.info)
        aux = aux.ant
