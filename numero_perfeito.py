# leia um numero e diga se é perfeito, um numeor é perfeito quando ele é igual
# a soma dos seus divisores

n = int(input('digite o numero: '))
soma = 0
for i in range(1, (n//2)+1):
    if n % i == 0:
        soma += i
print('é perfeito') if n == soma else print('não é perfeito')
