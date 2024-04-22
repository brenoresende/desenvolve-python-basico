'''
4) Você é mestre de uma mesa de RPG e vai criar um sistema para validar
uma ficha de personagem. Cada personagem tem uma classe específica com
requisitos de atributos. Escreva um script que solicita a classe de personagem
escolhida (guerreiro, mago ou arqueiro), os pontos de força e os pontos de
magia atribuídos ao personagem. O programa deve imprimir True se os pontos
de atributo são consistentes com a classe escolhida, seguindo as seguintes
regras:
Guerreiro: Força deve ser igual ou superior a 15, Magia deve ser 10 ou menos.
Mago: Força deve ser 10 ou menos, Magia deve ser igual ou superior a 15.
Arqueiro: Força e Magia devem ser ambos superiores a 5, mas nenhum deles
pode ser superior a 15.
O programa deve imprimir False se os pontos de atributo não são consistentes
com a classe escolhida. Segue um exemplo de interação com seu código no
terminal, com entradas de dados destacadas em laranja e as impressões de
seu código em branco.
'''

classe = input('\nInforme a classe escolhida: ')
forca = int(input('Digite os pontos de força: '))
magia = int(input('Informe os pontos de magia: '))

guerreiro = classe == "guerreiro" and forca >= 15 and magia <= 10
mago = classe == "mago" and magia >= 15 and forca <= 10
arqueiro = classe = "arqueiro" and magia >5 and forca > 5 and forca <= 15 and magia <= 15

print(f'Ponto de atributos consistentes com a classe escolhida: {guerreiro or mago or arqueiro}\n')


