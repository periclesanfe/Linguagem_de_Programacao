def eh_primo(n):
    if n > 1:
        for i in range(2, (n // 2) + 1):
            if (n % i == 0):
                return False
        else:
            return True
    else:
        return False


while True:
    n = int(input())
    if n == 0:
        break
    else:
        print('O número é primo') if eh_primo(n) else print('O número não é primo')
