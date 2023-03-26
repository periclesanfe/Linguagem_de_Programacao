# description: ambrósio comprou um novo jogo de tabuleiro que veio com peças faltando e decidiu joga-lo de outro jeito: cada rodada o jogador deve rolar o dado para conferir o número de casas que irá se mover, porém o dado está viciado e sempre dá o resultado na sequência 1,2,3,4,5,6,1,2,...
# O jogador que começar na casa 1(um), e se ultrapassar a ultima casa, deve retornar à primeira e continuar a andar o número de casas restantes, até para exatamente na ultima. Supondo que o número de casas seja 8 (oito), o jogador ocupará as seguintes posições: 1->2->4->7->3->8
# Como em alguns casso o número de jogadas pode ser grande, voce deve ajudar ambrósio a descobri-lo.
# a entrada vai ser o numero inteiro N que representa a ultima casa do tabuleiro (4<= N < 10000) Não ocorrerão jogos sem fim.
# saida vai ser o numero necessário de jogadas para conseguir chegar na ultima casa.

ultima_casa = int(input())
casa = 1
jogada = 1
dado = 1
while True:
    if dado > 6:
        dado = 1
    casa += dado
    if casa == ultima_casa:
        break
    elif casa > ultima_casa:
        casa = casa % ultima_casa
    jogada += 1
    dado += 1
print(jogada)
