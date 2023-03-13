def eh_primo(n):
    global contador
    contador += 1
    if n > 1:
        for i in range(2, (n // 2) + 1):
            if (n % i == 0):
                return False
        else:
            return True
    else:
        return False


contador = 0
max = 1000
lista = list(range(0, max))
for i in range(2, max):
    if lista[i] != 0:
        if eh_primo(i):
            for j in range(i * 2, max, i):
                lista[j] = 0
            print(i)
print(f'Total: {sum(lista)}')
print(f'Total de execuções: {contador}')
