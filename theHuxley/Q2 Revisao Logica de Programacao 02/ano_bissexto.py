def contar_digitos(n):
    if len(str(n)) == 4:
        return True
    return False


def eh_bissexto(n):
    if n % 4 == 0:
        if n % 100 != 0 or n % 400 == 0:
            return True
    return False


def mensagem(ano, eh):
    ano_atual = 2152
    if eh:
        if ano == ano_atual:
            print(f'O ano {ano} eh bissexto')
        elif ano < ano_atual:
            print(f'O ano {ano} foi bissexto')
        else:
            print(f'O ano {ano} serah bissexto')
    else:
        print(f'O ano {ano} NAO eh bissexto')


while True:
    ano = int(input())
    eh = False
    if ano == -1:
        break
    if contar_digitos(ano):
        if eh_bissexto(ano):
            eh = True
        mensagem(ano, eh)
    else:
        print('Ano invalido')
