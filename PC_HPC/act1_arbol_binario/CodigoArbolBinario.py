class ArbolBinarioOrdenado:

    def __init__(self):
        self._raiz = None
        self._arbolIzdo = None
        self._arbolDcho = None

    def raiz(self):
        return self._raiz

    def arbolIzdo(self):
        return self._arbolIzdo

    def arbolDcho(self):
        return self._arbolDcho

    def estaVacio(self):
        return self._raiz is None

    def insertar(self, elemento):
        if self.estaVacio():
            self._raiz = elemento
            self._arbolIzdo = ArbolBinarioOrdenado()
            self._arbolDcho = ArbolBinarioOrdenado()
        elif elemento <= self._raiz:
            self._arbolIzdo.insertar(elemento)
        elif elemento > self._raiz:
            self._arbolDcho.insertar(elemento)

    def tieneElemento(self, elemento):
        if self.estaVacio():
            return False
        elif self._raiz == elemento:
            return True
        elif elemento < self._raiz:
            return self._arbolIzdo.tieneElemento(elemento)
        else:
            return self._arbolDcho.tieneElemento(elemento)

    def numElementos(self):
        if self.estaVacio():
            return 0
        else:
            return 1 + self._arbolIzdo.numElementos() + self._arbolDcho.numElementos()

    def preOrden(self):
        if self.estaVacio():
            return []
        l = [self._raiz]
        l += self._arbolIzdo.preOrden()
        l += self._arbolDcho.preOrden()
        return l

    def inOrden(self):
        if self.estaVacio():
            return []
        l = self._arbolIzdo.inOrden()
        l.append(self._raiz)
        l += self._arbolDcho.inOrden()
        return l
