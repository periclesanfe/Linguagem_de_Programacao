# Description: criar um programa para identificar se um dia da semana digitado pelo usuário é um dia útil, final de semana ou inválido (considerar os seguintes dias como final de semana: sábado e domingo)

dias = {
    'segunda': 'de semana, útil.',
    'terça': 'de semana, útil.',
    'quarta': 'de semana, útil.',
    'quinta': 'de semana, útil.',
    'sexta': 'de semana, útil.',
    'sábado': 'final de semana',
    'domingo': 'final de semana'
}

dia = input('Digite o dia da semana: ').lower()
if dia not in dias:
    print('Dia inválido')
else:
    print(dia, 'é um dia de', dias[dia])
