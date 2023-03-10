# Description: criar um programa para identificar se um dia da semana digitado pelo usuário é um dia útil, final de semana ou inválido (considerar os seguintes dias como final de semana: sábado e domingo)

dias = {
    1: 'segunda-feira édia útil',
    2: 'terça-feira é dia útil',
    3: 'quarta-feira é dia útil',
    4: 'quinta-feira é dia útil',
    5: 'sexta-feira é dia útil',
    6: 'sábado é final de semana',
    7: 'domingo é final de semana'
}

dia = int(input('Digite o dia da semana: ').lower())
if dia not in dias:
    print('Dia inválido')
else:
    print(dias[dia])
