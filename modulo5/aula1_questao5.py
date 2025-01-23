'''
Você está trabalhando em um sistema de mensagens instantâneas, que deve permitir o uso de emojis nas conversas entre pessoas.

Seu programa deve apresentar para o usuário a lista de emojis disponíveis com o texto correspondente a cada emoji. 
Em seguida, solicite uma frase codificada ao usuário e apresente ela decodificada com a visualização de emojis (emojizada).

'''


print("Emojis disponíveis:\n")
print("❤️ - :red_heart:")
print("👍 - :thumbs_up:")
print("🤔 - :thinking_face:")
print("🥳 - :partying_face:")

# Solicita uma frase codificada ao usuário
frase_codificada = input("\nDigite uma frase e ela será emojizada:\n")

# Substitui os códigos pelos emojis correspondentes
frase_emojizada = frase_codificada.replace(":red_heart:", "❤️")
frase_emojizada = frase_emojizada.replace(":thumbs_up:", "👍")
frase_emojizada = frase_emojizada.replace(":thinking_face:", "🤔")
frase_emojizada = frase_emojizada.replace(":partying_face:", "🥳")

# Exibe a frase emojizada
print("\nFrase emojizada:")
print(frase_emojizada)













