'''
Crie a função encrypt() que recebe uma lista de strings e retorna os nomes criptografados, bem como a chave da criptografia. Regras:

 - Chave de criptografia: gere um valor n aleatório entre 1 e 10
 - Substitua cada caracter c pelo caracter c + n. Trabalharemos apenas com o intervalo de caracteres visíveis (entre 33 e 126 na tabela Unicode)
'''


import random

def encrypt(nomes):
    n = random.randint(1, 10)  
    nomes_cript = []
    for nome in nomes:
        nome_cript = ""
        for c in nome:
            c_code = ord(c) + n
            if c_code > 126:
                c_code -= 94
            nome_cript += chr(c_code)
        nomes_cript.append(nome_cript)
    return nomes_cript  

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_cript = encrypt(nomes)

print(f"nomes_cript = {nomes_cript}")