def get_frequencies(chain):
    total = len(chain)
    counter = {}
    for letter in chain:
        # añadimos la letra al diccionario si es la primera vez que aparece
        if letter not in counter.keys():
            counter[letter] = 0
        counter[letter] += 1 / total
    return counter
class Node:
    prob = 0.0
    symbol = ""
    encoding = ""
    used = False
    parent = -1 # se inicializa como -1 para ser coherente en los primeros hijos del nodo raíz
class HuffmanTree:
    
    def __init__(self, dict_probs):
        self.__probs = dict_probs
        self.Nodes = list()
        self.dictEncoder = {}
        self.__initNodes()
        self.__buildTree()
        dictEncoder = {}
        # Construimos el diccionario de códigos directamente en la construcción del árbol
        self.buildEncodingDictionary()
        
    def __initNodes(self):
        """ Con este método almacenamos en objetos Node toda la 
            info de nuestro diccionario de frecuencias"""
        for key, value in self.__probs.items():
            node = Node()
            node.prob = value
            node.symbol = key
            self.Nodes.append(node)
            
    def __buildTree(self):
        """ Se construye el árbol con la máxima iterativa de ir emparejando los nodos de menor probabilidad
        para generar un nuevo nodo (padre de los dos anteriores)"""
        indexMin1 = self.pop()
        indexMin2 = self.pop()
        while indexMin1 != -1 and indexMin2 != -1: # si alguno fuera -1 estaríamos terminando
            node = Node()
            prob1 = self.Nodes[indexMin1].prob
            prob2 = self.Nodes[indexMin2].prob
            node.prob = prob1 + prob2
            self.Nodes.append(node) # este nodo se convierte en el padre de los dos nodos usados y se añade al final de la lista
            self.Nodes[indexMin1].parent = len(self.Nodes) - 1
            self.Nodes[indexMin2].parent = len(self.Nodes) - 1
            # Asignamos código 1 al nodo de menor probabilidad
            self.Nodes[indexMin1].encoding = "1"
            self.Nodes[indexMin2].encoding = "0"
            indexMin1 = self.pop()
            indexMin2 = self.pop()
            
    def pop(self):
        """ Este método sirve para extraer los nodos en orden de prioridad (menor prob a mayor). Al contrario que en las 
        pilas o colas usadas, no voy eliminando los nodos, por eso incluyo el atributo used, para saber cuáles
        he usado ya """
        minProb = 1.0 # para que asigne valores en la primera iteración
        indexMin = -1 # valor de control para el caso en el que llegamos a terminar, en el que no actualizamos nada
        for i in range(len(self.Nodes)):
            if self.Nodes[i].prob <= minProb and not self.Nodes[i].used:
                minProb = self.Nodes[i].prob
                indexMin = i
        if indexMin != -1:
            self.Nodes[indexMin].used = True
        return indexMin

    def symbol_to_code(self, a):
        """ Asignamos a un símbolo dado su código binario Huffman """
        found = False
        for i in range(len(self.Nodes)):
            if self.Nodes[i].symbol == a:
                found = True
                ind = i
                break
        encoding = ""
        if found:
            while ind != -1:
                encoding += self.Nodes[ind].encoding
                ind = self.Nodes[ind].parent
        else:
            return "unknown symbol"
        return encoding[::-1] # le damos la vuelta al código porque lo hemos leído de abajo a arriba

    def buildEncodingDictionary(self):
        for symbol in self.__probs.keys():
            self.dictEncoder[symbol] = self.symbol_to_code(symbol)
            
    def decode(self, code):
        parent = len(self.Nodes) - 1 # índice de la raíz del árbol 
        for side in code:
            index_son = self.search_son(parent, side)
            parent = index_son
        return self.Nodes[index_son].symbol        

    def search_son(self, parent: int, side: str):
        for i in range(len(self.Nodes)):
            if self.Nodes[i].parent == parent and self.Nodes[i].encoding == side:
                return i            
        raise Error('Código no encontrado')

if __name__=='__main__':
    probs_enunciado = {"A":0.15,"B":0.3,"C":0.2,"D":0.05,"E":0.15,"F":0.05,"G":0.1}
    huffman1 = HuffmanTree(probs_enunciado)
    # Mostremos el diccionario de codificación (que construimos directamente dentro del constructor de la clase).
    huffman1.dictEncoder

    probs_enunciado_cheat = {"E":0.15,"B":0.3,"C":0.2,"D":0.05,"A":0.15,"F":0.05,"G":0.1}
    huffman1_cheat = HuffmanTree(probs_enunciado_cheat)
    # Mostremos el diccionario de codificación (que construimos directamente dentro del constructor de la clase).
    huffman1_cheat.dictEncoder
    pass