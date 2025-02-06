'''
Escreva um programa que solicite ao usuário inserir seu primeiro nome e sobrenome separadamente. 
Em seguida, concatene essas duas strings e exiba a mensagem de boas-vindas.

'''


primeiro_nome = input("Digite seu primeiro nome: ")


sobrenome = input("Digite seu sobrenome: ")


nome_completo = primeiro_nome + " " + sobrenome


print(f"Bem-vindo(a), {nome_completo}!")