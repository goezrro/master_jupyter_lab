import pandas as pd
import multiprocessing as mp
import numpy as np
import time
#modulo para usar expresiones regulares
import re
from multiprocessing import Pool
#importación del corpus brown
from nltk.corpus import brown


#funcion que construye el DataFrame para su procesamiento, on una frase por fila
def construye_textos():
    return [" ".join(np.random.permutation(sents)) for sents in brown.sents()]

#funcion que reemplaza comillas dobles
def reemplazar_comillas(texto):
    return texto.apply(lambda text: text.replace("``",'"'))

#funcion que convierte todas las palabras a minúsculas
#la función que pasa a minusculas es text.lower()
def a_minusculas(texto):
    return texto.lower()

#funcion que cuenta palabras de cada fila del dataframae
#separa las palabras en el texto de cada fila con split y devuelve la longitud de la lista de palabras
#la función que devuelve la lista de palabras es re.split(r"(?:\s+)|(?:,)|(?:\-)",text)
def contar_palabras(texto):
    pass
    
if __name__=='__main__':
    texto = construye_textos()
    texto = reemplazar_comillas(texto)
    texto = a_minusculas(texto)
    pass