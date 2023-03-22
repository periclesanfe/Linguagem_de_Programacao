# description: leet é uma maneira de escrever palavras na qual algumas letras, palavras ou silabas são substituidas por numeros ou símbolos. Isso é muito usado no contexto da informática para confundir leitores 'não iniciados' ou ecrever de forma resumida.trasforme um programa que transforma palavras na grafia comum em palavras na escrita leet ou de forma invertida.
# a, A = @
# e, E = 3
# i, I = 1
# o, O = 0
# t, T = 7
# s, S = 5

def verifica_entrada(entrada):
    if entrada == '':
        return 'Erro'
    for i in entrada:
        try:
            float(i)
        except ValueError:
            continue
        else:
            return 'Erro'
    return False


def substitui_numeros(string):
    global quantidade
    for i in range(0, len(string)):
        if string[i] == 'a':
            string[i] = '@'
            quantidade += 1
        elif string[i] == 'e':
            string[i] = '3'
            quantidade += 1
        elif string[i] == 'i':
            string[i] = '1'
            quantidade += 1
        elif string[i] == 'o':
            string[i] = '0'
            quantidade += 1
        elif string[i] == 't':
            string[i] = '7'
            quantidade += 1
        elif string[i] == 's':
            string[i] = '5'
            quantidade += 1
    return string


def separa_palavras(entrada):
    lista = []
    for i in entrada:
        lista.append(i)
    return lista


def leet_invertida(leet):
    for i in range(len(leet) - 1, -1, -1):
        if i == 0:
            print(leet[i], end='\n')
        else:
            print(leet[i], end='')


quantidade = 0
entrada = input().lower()
string = separa_palavras(entrada)
if verifica_entrada(string) == 'Erro':
    print('numeros')
else:
    leet = substitui_numeros(string)
    leet_invertida(leet)
print(quantidade)
