def equacao(n):
    lista = []
    while n != 1:
        lista.append(n)
        if n % 2 == 0:
            n = n//2
        else:
            n = (n*3)+1
    else:
        lista.append(n)

    return len(lista)


def maxima(par, impar):
    lista = []
    
    if(par < impar):
        par,impar=impar,par
        
    for index in range(impar, par+1, 1):
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
        #saida += str(pares.pop(0)) + " "
        #saida += str(impares.pop(0)) + " "
        saida += str(i) + " " + str(j) + " " + str(maximo) + '\n'

    return saida


lista_entrada = []
while True:
    try:
        entrada=input("").split()
        lista_entrada += entrada
    except:
        break

# ['1', '10', '100', '200', '201', '210', '900', '1000']

print(saida(lista_entrada))