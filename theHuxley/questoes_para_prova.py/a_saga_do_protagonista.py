# description: Z escreve dois numeros inteiros A e B, o desafio é fazer com que os dois numeros inteiros se tornem iguais usando o menor numero de movimentos.
# em um movimentos, tem as seguintes ações: escolher um dos numeros e somar 3, ou somar dois.
# entrada são dois inteiros 1 <= A, B <= 10^5
# saida deve ser impresso unico inteiro N, equivalente a quantidade minima de movimentos que o protagonista precisa fazer.

entrada = input().split()
A, B = int(entrada[0]), int(entrada[1])
contador = 0
while A != B:
    contador += 1
    if A > B:
        if (A - B) % 3 == 0:
            B += 3
        else:
            B += 2
    else:
        if (B - A) % 3 == 0:
            A += 3
        else:
            A += 2
print(contador)
