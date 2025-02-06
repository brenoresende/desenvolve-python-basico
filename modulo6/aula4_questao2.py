'''
Solicite uma frase do usuário e usando compreensão de listas imprima:

 - A lista de vogais da frase, ordenada alfabeticamente
 - A lista de consoantes da frase (remova espaços em branco)
'''


frase = input("Digite uma frase: ").lower() 


vogais = "aeiou"
consoantes = "bcdfghjklmnpqrstvwxyz"


lista_vogais = sorted([letra for letra in frase if letra in vogais])


lista_consoantes = [letra for letra in frase if letra in consoantes]


print(f"Vogais ordenadas: {lista_vogais}")
print(f"Consoantes sem espaços: {lista_consoantes}")






