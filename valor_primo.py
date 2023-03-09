# Description: Verifica se um número é primo
user_input = input('Digite um valor: ')  # Recebe o valor do usuário
mult = 0  # Contador de múltiplos
# Verifica ate a metade do valor, pois o ultimo multiplo de n é n/2
for i in range(2, int(user_input) // 2):
    if int(user_input) % i == 0:  # se for multiplo
        print('múltiplo de ', i)
        mult += 1
print('O número é primo') if mult == 0 else print(
    'O número não é primo e tem ', mult, ' múltiplos antes de ', user_input)  # Se não tiver múltiplos, é primo
