def readFile(name):
  with open(name,"r") as file:
    return file.read()

def wordCount(texto):
   return len(texto.split())

def uniqueWordCount(texto):
  return len(set(texto.split()))

def findContent(texto, palabra):
  return texto.count(palabra)

import re
def changeQuijoteToQuixote(texto):
  texto_original = r'Quijote'
  cambio="Quixote"
  return re.sub(texto_original,cambio,texto) 