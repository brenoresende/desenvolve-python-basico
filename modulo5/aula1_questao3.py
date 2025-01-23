'''
Escreva um programa em Python que utiliza a biblioteca random para gerar um número aleatório entre 1 e 10 e peça ao usuário para adivinhar o número. 
Forneça feedback se o palpite é muito alto, muito baixo ou correto. Interrompa a execução somente quando o usuário acertar o palpite.
'''



from random import randint 


n = int(input('Adivinhe o número entre 1 e 10: '))
a = randint(1, 10)

while n != a:
    if n > a:
        print('Muito alto, tente novamente!')
        n = int(input('Adivinhe o número entre 1 e 10: '))
    else:
        print('Muito baixo, tente novamente!')
        n = int(input('Adivinhe o número entre 1 e 10: '))
                
        
print(f'Correto! O número é {n}')










