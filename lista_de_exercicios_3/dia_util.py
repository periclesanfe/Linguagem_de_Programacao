dias = {1: 'Domingo', 2: 'Segunda', 3: 'Terça',
        4: 'Quarta', 5: 'Quinta', 6: 'Sexta', 7: 'Sábado'}
dia = int(input('Digite um número de 1 a 7: '))
print('{}-Feira é dia util'.format(dias[dia])) if dia in range(
    2, 6) else print('O dia {} é um dia de final de semana'.format(dias[dia]))
