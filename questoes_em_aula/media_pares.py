# calcule e mostre a média dos numeros pares entre 1 e N, incluindo os dois

n = int(input('Digite um número: '))
soma = 0
quantidade = 0.0
for i in range(1, n + 1, 2):
    soma += i
    quantidade += 1
print(soma / quantidade)
