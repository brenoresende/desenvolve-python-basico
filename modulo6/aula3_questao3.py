'''
Crie uma lista com 20 elementos, entre -10 e 10, gerados aleatoriamente. 
Em seguida encontre o intervalo que possui a maior quantidade de números negativos e delete ele da lista com o operador del. 
Você deve imprimir a lista antes e depois da deleção.
'''

from random import randint

lista = []

for elementos in range(20):
    lista.append(randint(-10,10))

print(f'Lista: {lista}')


maior_contagem = 0
melhor_inicio = 0


for i in range(len(lista)):
    for j in range(i + 1, len(lista) + 1):  
        sublista = lista[i:j]
        negativos = sum(1 for num in sublista if num < 0)  
        
        if negativos > maior_contagem:
            maior_contagem = negativos
            melhor_inicio = i
            melhor_fim = j


del lista[melhor_inicio:melhor_fim]

print("Lista após a remoção:", lista)
