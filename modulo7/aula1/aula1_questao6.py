'''
Dada uma string e uma palavra objetivo, encontre todos os anagramas da palavra objetivo. 
Anagramas são palavras com os mesmos caracteres rearranjados.
'''


from collections import Counter

def encontrar_anagramas(texto, palavra_alvo):
    palavras = ''.join(c for c in texto.lower() if c.isalnum() or c.isspace()).split()
    anagramas = []
    contagem_alvo = Counter(palavra_alvo)

    for palavra in palavras:
        contagem_palavra = Counter(palavra)
        if contagem_palavra == contagem_alvo and palavra != palavra_alvo:
            anagramas.append(palavra)

    return anagramas

texto = "Meu amor mora em Roma e me deu um ramo de flores"
palavra_alvo = "amor"
anagramas = encontrar_anagramas(texto, palavra_alvo)
print(f"Anagramas: {anagramas}")