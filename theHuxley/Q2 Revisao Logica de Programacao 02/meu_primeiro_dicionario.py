# description: criar um dicionario com todas as palavras  do texto em ordem alfabetica, palavras escritas com as mesmas letras deverão ser consideradas as mesmas palavras, como 'Apple', 'appel' e 'APPLE'. O fim da entrada é indicada por -1. Caracteres especiais ."(*$#: devem ser excluidos. Para remover esses especiais deve criar uma função cmada remover_epeciais que recebe uma string chamada de palavra. a função retorna uma string sem os caracteres especiais. Você deve imprimir uma lista de diferentes palavras que aparecem no texto, uma palavra por linha. Todas as palavras devem ser impressas com letras minúsculas, em ordem alfabética e com a quantidade de vezes que elas aparecem no texto. Deverá haver no máximo 5000 palavras distintas.

import re


# Define uma função para remover caracteres especiais de uma palavra
def remover_especiais(palavra):
    # Define uma expressão regular para corresponder aos caracteres especiais
    padrao = r'[."(*$#:]+'
    # Usa o método re.split() para dividir a palavra em pedaços usando a expressão regular
    pedacos = re.split(padrao, palavra)
    # Retorna os pedaços da palavra sem os caracteres especiais
    return pedacos


# Cria um dicionário vazio
dicionario_do_andy = {}


while True:
    # Lê entrada do usuário e a converte para minúsculas
    entrada = input().lower()
    if entrada == '-1':
        break
    else:
        linha_de_texto = entrada.split()
        for i in range(len(linha_de_texto)):
            # Usa a função remover_especiais() para dividir a palavra em pedaços sem caracteres especiais
            pedacos = remover_especiais(linha_de_texto[i])
            for p in pedacos:
                # Verifica se o pedaço não está vazio
                if p:
                    # Se o pedaço não estiver no dicionário, adiciona com contagem 1
                    if p not in dicionario_do_andy:
                        dicionario_do_andy[p] = 1
                    # Se o pedaço já estiver no dicionário, incrementa sua contagem
                    else:
                        dicionario_do_andy[p] += 1

# Ordena o dicionário em ordem alfabética e imprime cada palavra e sua contagem em uma linha separada
for chave, valor in sorted(dicionario_do_andy.items()):
    print(f'{chave} {valor}')
