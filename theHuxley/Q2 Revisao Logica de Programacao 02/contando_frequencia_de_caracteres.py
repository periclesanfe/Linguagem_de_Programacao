# description: Escreva um programa que receba um texto em uma única linha e imprima cada caractere e o número de vezes que ocorre no texto, na ordem inversa à alfabética.
# Uma linha contendo qualquer caractere, que pode incluir letras, números, pontuação e caracteres especiais.
# Uma sequência linhas onde cada linha contém um caractere e seu respectivo número de ocorrências no texto. A sequência de caracteres segue a ordem alfabética decrescente.

entrada = input()
dicionario = {}
for i in entrada:
    if i not in dicionario:
        dicionario[i] = 1
    else:
        dicionario[i] += 1
for chave, valor in sorted(dicionario.items(), reverse=True):
    print(f'{chave} {valor}')
