# while True:
#     entrada = input().split()
#     horas = list(map(int, entrada))
#     minutos = 0
#     if horas == ['0', '0', '0', '0']:
#         break
#     if horas[3] < horas[1]:
#         horas[3] = str(int(horas[3]) + 60)
#         horas[2] = str(int(horas[2]) - 1)
#     if horas[2] < horas[0]:
#         horas[2] = str(int(horas[2]) + 24)

#     minutos += int(horas[3]) - int(horas[1])
#     minutos += (int(horas[2]) - int(horas[0])) * 60
#     print(int(minutos))

def tudo_para_minuto(hora, minuto):
    if hora == 0:
        hora = 24
    return hora * 60 + minuto


while True:
    entrada = input().split()

    if entrada == ['0', '0', '0', '0']:
        break

    minutos = list(map(int, entrada))
    tempo1 = tudo_para_minuto(minutos[0], minutos[1])
    tempo2 = tudo_para_minuto(minutos[2], minutos[3])

    if tempo1 > tempo2:
        hora = tudo_para_minuto(24, 0)
        resultado = tempo2 + hora - tempo1
    else:
        resultado = tempo2 - tempo1

    print(resultado)
