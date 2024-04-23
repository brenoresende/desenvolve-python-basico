'''
1) Escreva um programa que lê dois números e informa se a sua soma é par ou ímpar. 
Critério: se o resto da divisão do número por 2 for 0, o número é par, caso contrário é ímpar. 
Lembre-se do operador do python % que retorna o resto de uma divisão.
'''

n1 = int(input('\nInforme o primeiro número da soma: '))
n2 = int(input('Informe o segundo número da soma: '))

soma = (n1+n2)%2

if soma:
    print('A soma dos números é impar!\n')
else: 
    print('A soma dos números é par!\n')




