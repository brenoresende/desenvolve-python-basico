'''
Preencha duas listas (lista1, lista2) com 20 valores inteiros aleatórios entre 0 a 50. 
Crie uma terceira lista interseccao contendo apenas os valores que se repetem nas duas listas. 
Ao final imprima:

 - Ambas as listas
 - A lista intersecção ordenada
 - A quantidade de vezes que cada elemento aparece em cada lista
'''

from random import randint
from collections import Counter


lista1 = [randint(0, 50) for i in range(20)] 
lista2 = [randint(0, 50) for i in range(20)]

interseccao = sorted(set(lista1) & set(lista2))

contagem_lista1 = Counter(lista1)
contagem_lista2 = Counter(lista2)

print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Lista Interseccao Ordenada: {interseccao}")
print(f"Frequência dos elementos na Lista 1: {contagem_lista1}")
print(f"Frequência dos elementos na Lista 2: {contagem_lista2}")









