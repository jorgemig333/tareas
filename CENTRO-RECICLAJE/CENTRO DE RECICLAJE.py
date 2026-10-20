
class Nodo:
    def __init__(self, codigo, descripcion):
        self.codigo = codigo
        self.descripcion = descripcion
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, codigo, descripcion):
        nuevo = Nodo(codigo, descripcion)
        # TODO 1: agrega el nodo al final sin perder los anteriores
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def mostrar(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.codigo, actual.descripcion)
            actual = actual.siguiente

    def esta_vacia(self):
        return self.cabeza is None

class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, elemento):
        # TODO 2: agrega el elemento a la cima
        self.items.append(elemento)

    def desapilar(self):
        # TODO 3: devuelve y elimina el último elemento;
        # controla el caso de pila vacía
        if len(self.items) == 0:
            return None
        return self.items.pop()

class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, elemento):
        # TODO 4: agrega el elemento al final
        self.items.append(elemento)

    def desencolar(self):
        # TODO 5: devuelve y elimina el primer elemento;
        # controla el caso de cola vacía
        if len(self.items) == 0:
            return None
        return self.items.pop(0)


# Pruebas con los datos asignados
lista = ListaEnlazada()
pila = Pila()
cola = Cola()

solicitudes = [
    ("REC01", "Papel"),
    ("REC02", "Plástico"),
    ("REC03", "Vidrio")
]

for solicitud in solicitudes:
    lista.agregar(solicitud[0], solicitud[1])
    pila.apilar(solicitud)
    cola.encolar(solicitud)

print("Lista enlazada:")
lista.mostrar()

print("\n¿La lista está vacía?")
print(lista.esta_vacia())

print("\nPrueba de pila (LIFO):")
while len(pila.items) > 0:
    print(pila.desapilar())

print("\nPrueba de cola (FIFO):")
while len(cola.items) > 0:
    print(cola.desencolar())

print("\nPrueba de estructura vacía:")
print("Pila vacía:", Pila().desapilar())
print("Cola vacía:", Cola().desencolar())

lista_vacia = ListaEnlazada()
print("Lista enlazada vacía:", lista_vacia.esta_vacia())
