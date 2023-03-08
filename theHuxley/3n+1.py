def equacao(n):
    lista = []
    while n != 1:
        lista.append(n)
        if n % 2 == 0:
            n = n/2
        else:
            n = (n*3)+1
    else:
        lista.append(n)

    return len(lista)


def maxima(par, impar):
    lista = []
    for index in range(par, impar):
        lista.append(equacao(index))
    return max(lista)


def separarEntrada(numeros):
    pares, impares = [], []
    for i in range(len(numeros)):
        num = int(numeros[i])
        if i % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    return pares, impares


def saida(numeros):
    pares, impares = separarEntrada(numeros)
    saida = ""

    for i, j in zip(pares, impares):
        maximo = maxima(i, j)
        saida += str(pares.pop(0)) + " "
        saida += str(impares.pop(0)) + " "
        saida += str(maximo) + '\n'

    return saida


input1 = input("")
input2 = input("")
input3 = input("")
input4 = input("")

# ['1', '10', '100', '200', '201', '210', '900', '1000']
entrada = input1.split() + input2.split() + input3.split() + input4.split()

print(saida(entrada))
