'''
Escreva um script em Python que solicita do usuário uma quantidade indefinida de números inteiros (com pelo menos 4 valores), 
os armazena em uma lista e, usando fatiamento de listas, imprima:

 - A lista original
 - Os 3 primeiros elementos
 - Os 2 últimos elementos
 - A lista invertida (do fim para o começo)
 - Os elementos de índice par (0, 2, 4 … )
 - Os elementos de índice ímpar (1, 3, 5, … )
'''


lista = []

num_elementos = 0

## Verifica se o número de elementos é válido e solicita novamente até que seja
while True:
    num_elementos = int(input("Informe o número de elementos que a lista terá (mínimo 4): "))
    if num_elementos < 4: 
        print("Valor inválido pois é menor que o mínimo. \n")
    else:
        break

## Recebe os números do usuário
for i in range(num_elementos):
    lista.append(int(input()))


print(lista)
print(lista[0:3])
print(lista[-2::])
print(lista[::2])
print(lista[1::2])


