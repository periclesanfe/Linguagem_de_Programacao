# description: Faça um programa que dado um número inteiro n, imprima n linhas, onde cada linha deve seguir o padrão de triangulo de números.

n = int(input())
for i in range(1, n + 1):
    output = ""
    for j in range(1, i + 1):
        output = output + str(i)
    print(output)
