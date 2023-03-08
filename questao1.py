# 1 - Crie um programa que leia um nome completo e imprima as iniciais

nomeCompleto = str(input('Digite seu nome completo: '))
nomeSeparado = nomeCompleto.split()
for i in nomeSeparado:
    print(i[0], end='')
