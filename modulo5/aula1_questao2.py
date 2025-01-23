'''
Escreva um código que gere n valores inteiros aleatórios entre 0 e 100 e calcule a raíz quadrada da soma dos valores. 
Peça ao usuário o valor de n

Biblioteca random: Função randint()
Biblioteca math:  Função sqrt()
'''

from math import sqrt
from random import randint 


n = int(input('Quantos valores devem ser gerados? '))
soma = 0

for  i in range(n):
    soma += randint(1, 100)

print(f'O valor da raiz dos números aleatóris gerados é de {round(sqrt(soma), 2)}')

