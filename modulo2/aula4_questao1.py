'''
1) Faça um programa para ler as dimensões de um terreno em inteiros
(comprimento e largura), bem como o preço do metro quadrado da região em
ponto flutuante. Calcule o valor do terreno e imprima o resultado como mostra
o exemplo a seguir:
O terreno possui 250m2 e custa R$512,490.50
Comente na linha acima de cada instrução uma breve descrição da instrução.
Fórmulas:
• area_m2 = comprimento * largura
• preco_total = preco_m2 * area_m2
'''


#Solicita e armazena o comprimento do terreno
comprimento = int(input('\nInforme o comprimento do terreno: '))

#Solicita e armazena a largura do terreno
largura = int(input('Informe a largura do terreno: '))

#Solicita e armazena o preço do m² do terreno
preco_m2 = float(input('Informe o preço por m² do terreno: '))

#Calcula a área do terreno em m²
area_m2 = comprimento * largura

#Calcula o preço total, baseado na área e preço por m²
preco_total = preco_m2 * area_m2

print(f'O terreno possui {area_m2}m2 e custa R${preco_total:,.2f}\n')









