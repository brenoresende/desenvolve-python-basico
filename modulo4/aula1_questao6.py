"""
Maria precisa de sua ajuda para organizar os experimentos de seu
laboratório. Ela quer saber no final do ano, quantas cobaias foram
utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada.
Este laboratório utiliza três tipos de cobaias: sapos, ratos e coelhos.
Entrada: A primeira linha de entrada é um inteiro N com a quantidade de
experimentos registrados. As N linhas seguintes contém um inteiro Quantia
que representa a quantidade de cobaias utilizadas e um caractere Tipo (S,
R ou C) com o tipo de cobaia (S:Sapo, R:Rato ou C:Coelho).
Saída: Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia
e o percentual de cada uma em relação ao total de cobaias utilizadas
"""


n = int(input())
i=0

soma_sapo = 0
soma_rato = 0
soma_coelho = 0

while i<n:
    qnt = int(input())
    op = input().upper()
    i += 1
    if op == 'S':
        soma_sapo += qnt
    if op == 'R':
        soma_rato += qnt
    if op == 'C':
        soma_coelho += qnt

total = soma_sapo + soma_rato + soma_coelho

print(f'Total: {total}')
print(f'Total de coelhos: {soma_coelho}')
print(f'Total de ratos: {soma_rato}')
print(f'Total de sapos: {soma_sapo}')
print(f'Percentual de coelhos: {soma_coelho/total*100:.2f} %')
print(f'Percentual de ratos: {soma_rato/total*100:.2f} %')
print(f'Percentual de sapos: {soma_sapo/total*100:.2f} %')

