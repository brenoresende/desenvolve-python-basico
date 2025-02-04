'''
Crie um programa em Python que receba duas listas de números do usuário, podendo cada lista ter uma quantidade diferente de valores. 
Em seguida, combine essas duas listas de forma alternada para formar uma terceira lista. 
Intercale os elementos até o final da primeira lista, adicionando ao final os elementos remanescentes da maior lista.

'''


num_elementos1 = int(input('Digite a quantidade de elementos da lista 1: '))
num_elementos2 = int(input('Digite a quantidade de elementos da lista 2: '))

lista1, lista2, intercalada = [], [], []


print(f'Digite os {num_elementos1} da lista 1: ')
for i in range(num_elementos1):
    lista1.append(int(input()))

print(f'Digite os {num_elementos2} da lista 2: ')
for i in range(num_elementos2):
    lista2.append(int(input()))

tamanho_min = min(len(lista1), len(lista2))


for i in range(tamanho_min):
    intercalada.append(lista1[i])
    intercalada.append(lista2[i])


intercalada.extend(lista1[tamanho_min:])
intercalada.extend(lista2[tamanho_min:])


print(f'Lista intercalada: {intercalada}')



