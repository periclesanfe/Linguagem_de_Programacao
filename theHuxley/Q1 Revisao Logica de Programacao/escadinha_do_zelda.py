# Descripion: Zelda e seus amigos tiveram uma brilhante ideia durante as aulas da monitoria da cadeira de introdução a programação: que tal fazer um programa que, dado um número n (1 <= n <= 40) printa na tela os numeros de 1 até o número da iteração atual, sendo que serão feitas n iterações

n = int(input())
for m in range(1, n + 1):
    output = ''
    for j in range(1, m + 1):
        if j == n + 1 or j == 1:
            output += str(j)
        else:
            output += ' ' + str(j)
    print(output)
