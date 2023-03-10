# Description: Criar um programa para identificar se um mês digitado pelo usuário é de alta ou baixa temporada (considerar os seguintes meses como alta temporada: dezembro, janeiro, fevereiro, julho)

meses = {
    'janeiro': 'alta',
    'fevereiro': 'alta',
    'abril': 'baixa',
    'maio': 'baixa',
    'junho': 'baixa',
    'julho': 'alta',
    'agosto': 'baixa',
    'setembro': 'baixa',
    'outubro': 'baixa',
    'novembro': 'baixa',
    'dezembro': 'alta'
}

mes = input('Digite o mês: ').lower()
if mes in meses:
    print(mes, 'é um mês de', meses[mes], 'temporada')
