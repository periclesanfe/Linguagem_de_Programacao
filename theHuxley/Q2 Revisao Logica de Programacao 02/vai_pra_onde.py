# Description:Ester está programando suas férias e decidiu viajar gastando no máximo R$ 300 de passagens (ida e volta). Para usar bem seu dinheiro, ela quer ir para a cidade mais longe possível sem extrapolar seu orçamento. Escreva um programa que receba como entrada o nome, a distância (em quilômetros) e o valor da passagem (só ida) de várias cidades, até que ela informe a cidade FIM, e exiba o nome do melhor destino para ela.
# Obs: Considere que as passagens de ida e de volta tenham o mesmo valor
# Input: Um String (que pode estar escrito de qualquer forma), um inteiro (km) e um real para cada cidade
# Para encerrar a entrada, será informado o String FIM (escrito de qualquer forma) como nome da cidade
# Um String com as letras todas maiúsculas
# Se nenhuma cidade for informada, deverá ser exibida a mensagem SEM DESTINO

cidade_mais_distante = None
maior_distancia = 0

while True:
    cidade = input().upper()
    if cidade == 'FIM':
        break
    distancia = input()
    preco_passagem = input()

    if int(distancia) > maior_distancia and float(preco_passagem) <= 150.0:
        cidade_mais_distante = cidade
        maior_distancia = int(distancia)

if cidade_mais_distante:
    print(cidade_mais_distante)
else:
    print('SEM DESTINO')
