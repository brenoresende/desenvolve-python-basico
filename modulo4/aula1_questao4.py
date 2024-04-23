#Recebimento e armazenamento dos dados
n = int(input('\nDigite um número: '))
maior = 0

#Processamento e impressão
while n > 0:
    x = int(input('Digite outro número: '))
    if x> maior:
        maior = x
    n -= 1

print(f'O maior número digitado é {maior}\n')
