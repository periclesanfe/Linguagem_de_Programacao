candidatos = {}

while True:
    entrada = input()
    if entrada == 'FIM':
        break
    nome, quanti = entrada.split()
    preco = 0
    if nome not in candidatos.keys():
        candidatos[nome] = nome, 0
    for i in range(int(quanti)):
        tipo = input()
        if tipo == 'internet':
            preco += 3000
        elif tipo == 'revista':
            preco += 750
        elif tipo == 'outdoor':
            preco += 1500
        elif tipo == 'radio' or tipo == 'tv':
            info = input()
            if info == 'fm':
                preco += 500
            elif info == 'am':
                preco += 300
            elif int(info) <= 20:
                preco += 1200
            elif int(info) > 20:
                preco += 2000
    candidatos[nome] = nome, preco

for candidato in candidatos:
    print('{}: {:.2f}'.format(candidato, candidatos[candidato][1]))
