# Description: Seu objetivo é escrever um programa que calcule a soma dos elementos dados na entrada.
# Entrada: Consiste de um número inteiro n indicando a quantidade de elementos a serem lidos seguidos de n elementos, um em cada linha.
# Atenção, considere: n <=10000.
# Consiste de um número inteiro indicando a soma, seguido de um final de linha.

while True:
    try:
        n = int(input())
        if n == '':
            raise ValueError
        soma = 0
        for i in range(n):
            soma += int(input())
    except ValueError:
        print('String deve ter no máximo 50 caracteres.')
        continue
    print(f'{soma} ')
    break
