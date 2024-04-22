'''
1) Juliana e Cris querem entrar em um bar, mas só podem se ambos forem
maiores de idade (>17). Escreva um programa que solicite as idades de Juliana
e Cris e imprima True se ambas forem maiores de 17 anos, indicando que podem
entrar no bar, e False caso contrário.
'''


#Solicita e armazena a idade de Juliana e Cris
juliana = int(input('Informe a idade de Juliana: '))
cris = int(input('Informe a idade de Cris: '))

#Imprime true se ambas forem maior de idade e False caso, no mínimo, uma dela não seja
print(juliana > 17 and cris > 17)

