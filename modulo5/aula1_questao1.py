'''
Desenvolva um programa em Python que peça ao usuário para inserir dois números decimais e calcule a diferença absoluta entre esses dois números. 
Utilize a função nativa abs para garantir que o resultado seja sempre positivo e round para arredondar o resultado para duas casas decimais.
'''



# Solicita inserção de dois números decimais
n1 = float(input("Digite o primeiro número decimal: "))
n2 = float(input("Digite o segundo número decimal: "))

# Cálculo da diferença e arredondamento para duas casas
diferenca_absoluta = round(abs(n1 - n2), 2)

# Exibe o resultado
print(f"A diferença absoluta entre os números é:: {diferenca_absoluta}.")



