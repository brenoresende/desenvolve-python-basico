'''
Escreva um programa em Python que utiliza a biblioteca datetime para exibir a data e hora atuais com a formatação apresentada a seguir:
'''


from datetime import datetime

# Obtém a data e hora atuais
agora = datetime.now()

# Formata a data e a hora
data_formatada = agora.strftime("%d/%m/%Y")
hora_formatada = agora.strftime("%H:%M")

# Exibe o resultado
print(f"Data: {data_formatada}")
print(f"Hora: {hora_formatada}")



