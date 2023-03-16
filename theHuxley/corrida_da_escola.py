# description: A escola de Joãozinho tradicionalmente organiza uma corrida ao redor do prédio. Como todos os alunos são
# convidados a participar e eles estudam em períodos diferentes, é difícil que todos corram ao mesmo tempo.
# Para contornar esse problema, os professores cronometram o tempo que cada aluno demora para dar cada volta
# ao redor da escola, e depois comparam os tempos para descobrir a classificação final.
# Sua tarefa é, sabendo o número de competidores, o número de voltas de que consistiu a corrida e os tempos
# de cada aluno competidor, descobrir quem foi o aluno vencedor, para que ele possa receber uma medalha comemorativa.

NeM = list(map(int, input().split()))
ganhador = 0
menor_tempo = 0


for i in range(0, NeM[0]):
    n = list(map(int, input().split()))
    soma = sum(n)

    if ganhador == 0:
        ganhador = i + 1
    if menor_tempo == 0:
        menor_tempo = soma

    if soma < menor_tempo:
        menor_tempo = soma
        ganhador = i + 1

print(ganhador)
