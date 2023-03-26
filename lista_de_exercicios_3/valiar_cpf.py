def calculo(cpf, multi, digito_final):
    soma = 0
    for i in range(0, len(cpf)):
        if i < digito_final:
            n = int(cpf[i]) * multi  # passo1/6
            soma += n  # passo2/7
            multi -= 1
    resultado = 11 - (soma % 11)  # passo3/8 e passo4/9
    return resultado


cpf = input('Digite o CPF: ')
resultado1 = calculo(cpf, 10, 9)  # passo5
while True:
    if resultado1 == int(cpf[9]) or int(cpf[9]) == 0:
        resultado2 = calculo(cpf, 11, 10)
    else:
        print('cpf inválido')
        break

    if resultado2 == int(cpf[10]) or int(cpf[10]) == 0:
        print('cpf válido')
        break
    else:
        print('cpf inválido')
        break

    # if resultado1 < 10:
    #     if resultado1 == int(cpf[9]):
    #         resultado2 = calculo(cpf, 11, 10)  # passo10
    #     else:
    #         print('CPF inválido 1')

    #         break
    # else:
    #     if int(cpf[9]) == 0:
    #         resultado2 = calculo(cpf, 11, 10)  # passo10
    #     else:
    #         print('CPF inválido 2')
    #         break

    # if resultado2 < 10:
    #     if resultado2 == int(cpf[10]):
    #         print('CPF válido')
    #         break
    #     else:
    #         print('CPF inválido 3')
    #         break
    # else:
    #     if int(cpf[10]) == 0:
    #         print('CPF válido')
    #         break
    #     else:
    #         print('CPF inválido 4')
    #         break
