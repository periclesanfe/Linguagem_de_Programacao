# Description: Criar um programa que identifique o valor a ser pago por um plano de saúde dada a idade do conveniado considerando que todos pagam R$ 100 mais um adicional conforme a seguinte tabela:
# 1) crianças com menos de 10 anos pagam R$ 80;
# 2) conveniados com idade entre 10 e 30 anos pagam R$ 50;
# 3) conveniados com idade acima de 40 e 60 anos pagam R$ 95;
# 4) conveniados com idade acima de 60 anos pagam R$ 130.

idade = int(input('Digite a idade do conveniado: '))
if idade < 10:
    print('O valor a ser pago é R$ 180,00')
elif 10 <= idade <= 30:
    print('O valor a ser pago é R$ 150,00')
elif 40 < idade < 60:
    print('O valor a ser pago é R$ 195,00')
elif idade >= 60:
    print('O valor a ser pago é R$ 230,00')
