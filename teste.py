def equacao(n):
    ciclo = 1
    while n > 1:
        if n % 2 == 0:
            n = n//2
        else:
            n = (n*3)+1
        ciclo += 1

    return ciclo


def maxima(par, impar):

    if (par < impar):
        par, impar = impar, par

    max = equacao(impar)

    for index in range(impar+1, par+1):
        res = equacao(index)
        if res > max:
            max = res

    return variavel


def separarEntrada(numeros):
    primeiros, segundos = [], []
    for i in range(len(numeros)):
        num = int(numeros[i])
        if i % 2 == 0:
            primeiros.append(num)
        else:
            segundos.append(num)
    return primeiros, segundos


def saida(numeros):
    primeiros, segundos = separarEntrada(numeros)
    saida = ""

    for i, j in zip(primeiros, segundos):
        maximo = maxima(i, j)
        saida += str(i) + " " + str(j) + " " + str(maximo) + '\n'

    return saida


lista_entrada = []
while True:
    try:
        entrada = input("").split()
        lista_entrada += entrada
    except:
        break

print(saida(lista_entrada))
