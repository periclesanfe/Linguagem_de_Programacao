# Description: Criar um programa para calcular o valor da multa a ser paga de anuidade de uma associação. A unidade deve ser paga no mês de janeiro. Por mês, é cobrado 5% de juros (com juros sobre juros). Por exemplo, uma associação de R$ 100 paga em janeiro, custa R$ 100; em fevereiro, custa R$ 105; em março, custa R$ 110,25; e em dezembro, custa R$ 171,03.

mes = float(input('Digite o numero do mês de pagamento: '))
preco = 100.00
while mes > 1:
    preco = preco + (preco * 0.05)
    mes -= 1
print(r'O preço da anuidade é: R$ {:.2f}'.format(preco))
