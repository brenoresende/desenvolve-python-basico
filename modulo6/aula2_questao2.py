'''
Faça um programa que gere aleatoriamente um valor entre 5 e 20 e armazene em uma variável chamada num_elementos. 
Em seguida gere aleatoriamente valores entre 1 e 10 em quantidade correspondente a num_elementos, e armazene em uma lista chamada elementos. 
Em seguida imprima:

 - A lista elementos
 - A soma dos valores da lista
 - A média dos valores da lista
'''

from random import randint


num_elementos = randint(5, 20)
elementos = []
soma = 0

for i in range(num_elementos):
    elementos.append(randint(1, 10))


for i in range(num_elementos):
    soma += elementos[i]

print(f'Lista: {elementos}')
print(f'Soma: {soma}')
print(f'Média: {(soma/num_elementos):.2f}')



