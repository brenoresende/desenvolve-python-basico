'''
3) Você está desenvolvendo um programa para calcular o preço total de uma
compra em uma loja online. O preço dos produtos é calculado multiplicando a
quantidade pelo preço unitário. Escreva um programa em Python que solicite
do usuário o nome, o preço unitário e a quantidade de 3 produtos comprados e
imprima ao final o preço total da compra. Note no exemplo a seguir que:
-Cada entrada de dados tem uma mensagem indicando o dado solicitado
(mensagens em itálico, dado de entrada em negrito)
-A saída deve estar formatada exatamente como indicado (a string “Total: R$” e
o preço com um separador de milhar e duas casas decimais)
'''



# Solicitação de entrada para o produto 1
nome_produto_1 = input("\nDigite o nome do produto 1: ")
preco_unitario_1 = float(input("Digite o preço unitário do produto 1: ").replace(',', '.'))
quantidade_1 = int(input("Digite a quantidade do produto 1: "))

# Solicitação de entrada para o produto 2
nome_produto_2 = input("\nDigite o nome do produto 2: ")
preco_unitario_2 = float(input("Digite o preço unitário do produto 2: ").replace(',', '.'))
quantidade_2 = int(input("Digite a quantidade do produto 2: "))

# Solicitação de entrada para o produto 3
nome_produto_3 = input("\nDigite o nome do produto 3: ")
preco_unitario_3 = float(input("Digite o preço unitário do produto 3: ").replace(',', '.'))
quantidade_3 = int(input("Digite a quantidade do produto 3: "))

# Cálculo do total para cada produto
total_produto_1 = preco_unitario_1 * quantidade_1
total_produto_2 = preco_unitario_2 * quantidade_2
total_produto_3 = preco_unitario_3 * quantidade_3

# Cálculo do total de todos os produtos
total_geral = total_produto_1 + total_produto_2 + total_produto_3

# Exibição dos resultados com separador de casas de milhar
print(f"\nTotal: R${total_geral:,.2f}\n")
























