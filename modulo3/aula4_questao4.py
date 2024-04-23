'''
4) Você está implementando um sistema de entrega expressa e precisa calcular o valor do frete com base na distância e no peso do pacote. 
Escreva um código que solicita a distância da entrega em quilômetros e o peso do pacote em quilogramas. 
O programa deve calcular e imprimir o valor do frete de acordo com as seguintes regras:

Distância até 100 km: R$1 por kg.
Distância entre 101 e 300 km: R$1.50 por kg.
Distância acima de 300 km: R$2 por kg.
Acrescente uma taxa de R$10 para pacotes com peso superior a 10 kg
'''

d = int(input('\nInforme a distância em KM: '))
p = int(input('Informe o peso em KG: '))
frete = 0

if p > 10:
    frete += 10

if d > 0 and d <= 100:
    frete += p
elif d <= 300:
    frete += p*1.5
else:
    frete += p*2

if d > 0 and p > 0:
    print(f'O valor do frete é de R${frete:.2f}\n')
else:
    print(f'Um ou ambos valores digitados são inválidos!\n')

