'''
5) Um instituto realizou uma pesquisa de público e precisa calcular a
média de idade dos respondentes. Escreva um programa que leia um
inteiro N com a quantidade de respondentes e em seguida leia as N
idades de cada respondente. Ao final, imprima a média das idades.
(idade1 + idade2 + idade3 + … + idade_n)/N
'''

qnt = int(input('\nInforme a quantidade de respostas: '))
cont = 0
idade = 0
soma = 0

while qnt > 0:
    cont += 1
    idade = int(input('Informe a idade da pessoa: '))
    soma += idade
    qnt -= 1 

print(f'A média das idades é de {int(soma/cont)} anos! \n')


