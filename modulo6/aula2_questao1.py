'''
Faça um programa que gere aleatoriamente 20 valores inteiros entre -100 e 100 e os armazene em uma lista. Em seguida imprima na ordem estabelecida:

 - A lista ordenada, sem modificar a lista original
 - A lista original
 - O índice do maior valor da lista
 - O índice do menor valor da lista

'''

from random import randint

lista = []

for i in range(20):
    lista.append(randint(-100,100)) 

print(lista)

lista.sort()

print(lista)
print(lista[0])
print(lista[-1])


