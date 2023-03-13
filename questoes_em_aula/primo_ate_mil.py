def eh_primo(n):
    if n > 1:
        for i in range(2, (n // 2) + 1):
            if (n % i == 0):
                return False
        else:
            return True
    else:
        return False


soma = 0
for i in range(2, 1001):
    if eh_primo(i):
        print(f'{i} é primo')
        soma += i
    else:
        print(f'{i} não é primo')
print(soma)
