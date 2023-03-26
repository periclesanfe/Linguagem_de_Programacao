def movimentar(direcao):
    global x, y
    if direcao == 'c':
        x -= 1
    elif direcao == 'b':
        x += 1
    elif direcao == 'e':
        y -= 1
    elif direcao == 'd':
        y += 1


def posicao_oposta(direcao):
    if direcao == 'c':
        return 'b'
    elif direcao == 'b':
        return 'c'
    elif direcao == 'e':
        return 'd'
    elif direcao == 'd':
        return 'e'


x = 0
y = 0

entrada = input().split()
for i in entrada:
    movimentar(i)
movimentar(posicao_oposta(entrada[-2]))

print(f'Coordenada X:{x}, Y:{y}')
