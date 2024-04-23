#Recebimento e armazenamento dos dados
n1 = int(input('\nDigite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

#processamento e impressão
m = (n1 + n2 + n3) / 3

if m >= 60:
    print('Aprovado')
elif m >= 40:
    print('Recuperação')
else:
    print('Reprovado')

print('Fim\n')

