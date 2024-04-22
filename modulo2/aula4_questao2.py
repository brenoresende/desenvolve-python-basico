'''
2) Leia um valor inteiro correspondente a uma temperatura em graus Fahrenheit
e apresente-a convertida em graus Celsius.
Fórmula de conversão: C = (F - 32) * (5/9), sendo C o valor em graus Celsius e F o
valor em Fahrenheit. Antes de imprimir, converta o valor em Celsius para inteiro.
A mensagem deve estar formatada da seguinte maneira:
86 graus Fahrenheit são 30 graus Celsius.
'''

#Solicitando e armazenando o valor da temperatura em °F
f = int(input('\nInforme a temperatura em °F: '))

#Calculando a temperatura em °C
c = (f - 32) * (5/9)

#Mostrando para o usuário o valor da temperatura convertida para °C
print(f'{f} graus Fahrenheit são {int(c)} graus Celsius\n')


















