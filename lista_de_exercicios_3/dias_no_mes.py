# Description: construir um programa que identifica quantos dias há em um mês, sabdno o mês e o ano

# Dicionário que mostra o número de dias de cada mês
meses = {
    'janeiro': 31,
    'fevereiro (ano comum)': 28,
    'fevereiro (ano bissexto)': 29,
    'março': 31,
    'abril': 30,
    'maio': 31,
    'junho': 30,
    'julho': 31,
    'agosto': 31,
    'setembro': 30,
    'outubro': 31,
    'novembro': 30,
    'dezembro': 31
}


# Verifica se um ano é bissexto ou não
def eh_bissexto(ano):
    return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)


# Define o número de dias em fevereiro, com base no ano bissexto ou não
def dias_em_fevereiro(ano):
    if eh_bissexto(ano):
        return meses['fevereiro (ano bissexto)']
    else:
        return meses['fevereiro (ano comum)']


# Pede ao usuário o nome do mês
mes = input("Digite o nome do mês: ").lower()

# Pede ao usuário o ano
ano = int(input("Digite o ano: "))

# Verifica se o nome do mês é válido
if mes not in meses:
    print(f"Desculpe, {mes} não é um mês válido.")
else:
    # Exibe o número de dias do mês, com base no ano informado pelo usuário
    if mes.startswith('fevereiro'):
        dias = dias_em_fevereiro(ano)
    else:
        dias = meses[mes]
    print(f"{mes.capitalize()} tem {dias} dias em {ano}.")
