# description: A entrada é composta de quinze linhas, cada uma contendo o resultado de um jogo. A primeira linha contém o resultado do jogo de número 1, a segunda linha o resultado do jogo de número 2, e assim por diante. O resultado de um jogo é representado por dois números inteiros M e N separados por um espaço em branco, indicando respectivamente o número de gols da equipe representada à esquerda e à direita na tabela de jogos. Seu programa deve imprimir uma única linha, contendo a letra identificadora da equipe campeã, seguida de uma quebra de linha.

jogadores_oitavas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
jogadores_quartas = []
jogadores_semifinais = []
jogadores_final = []

jogador1 = 0
jogador2 = 1


while jogador2 < 16:
    resultado = input().split()
    if resultado[0] > resultado[1]:
        jogadores_quartas.append(jogadores_oitavas[jogador1])
    else:
        jogadores_quartas.append(jogadores_oitavas[jogador2])
    jogador1 += 2
    jogador2 += 2

jogador1 = 0
jogador2 = 1
while jogador2 < 8:
    resultado = input().split()
    if resultado[0] > resultado[1]:
        jogadores_semifinais.append(jogadores_quartas[jogador1])
    else:
        jogadores_semifinais.append(jogadores_quartas[jogador2])
    jogador1 += 2
    jogador2 += 2

jogador1 = 0
jogador2 = 1
while jogador2 < 4:
    resultado = input().split()
    if resultado[0] > resultado[1]:
        jogadores_final.append(jogadores_semifinais[jogador1])
    else:
        jogadores_final.append(jogadores_semifinais[jogador2])
    jogador1 += 2
    jogador2 += 2

resultado = input().split()
if resultado[0] > resultado[1]:
    print(jogadores_final[0])
else:
    print(jogadores_final[1])
