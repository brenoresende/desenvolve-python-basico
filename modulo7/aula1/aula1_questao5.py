'''
Implemente um código que leia uma string do usuário e imprima quantas vogais existem na frase e quais os seus índices da string. 
Dica: letra in "aeiou".
'''


frase = input("Digite uma frase: ").lower()
vogais = "aeiou"
num_vogais = 0
indices = []

for i in range(len(frase)):
    if frase[i] in vogais:
        num_vogais += 1
        indices.append(i)

print(f"{num_vogais} vogais")
print(f"Índices {indices}")