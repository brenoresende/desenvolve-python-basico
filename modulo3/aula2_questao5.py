'''
5)Solicite de um usuário seu gênero (“M” ou “F”), sua idade e seu tempo de
serviço (em anos) e escreva uma expressão que imprima True se a pessoa já
pode se aposentar, ou False caso contrário, de acordo com as seguintes regras:
A: Para mulheres, ter mais de 60 anos. Para homens, 65.
B: Ou ter trabalhado pelo menos 30 anos
C: Ou ter 60 anos e trabalhado pelo menos 25.
'''

genero = input('\nInforme o seu gênero (M ou F): ').lower()
idade = int(input('Informe sua idade: '))
servico = int(input('Informe seu tempo de serviço em anos: '))

m = genero == "m" and (idade >= 65 or servico >= 30) and (idade >= 60 or servico >= 25)
f = genero == "f" and (idade >= 60 or servico >= 30) 

print(f'{m or f}\n')

