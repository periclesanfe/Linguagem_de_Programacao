import os
import time


def adicionar_pessoa():
    nome = input("Digite o nome: ")
    cpf = input("Digite seu CPF: ")
    onde_mora = input("Digite onde mora: ")
    ano_nascimento = input("Digite o ano de nascimento: ")

    return nome, cpf, onde_mora, ano_nascimento


def buscar_cpf(cpf):
    for pessoa in lista:
        if pessoa[1] == cpf:
            return pessoa
    return 'Essa pessoa não existe no banco de dados'


def listar_nomes():
    retorno = ''
    for pessoa in lista:
        retorno += pessoa[0] + ', '
    return retorno


def listar_cidades():
    retorno = ''
    for pessoa in lista:
        if pessoa[2] not in retorno:
            retorno += pessoa[2] + ', '
    return retorno


def menu():
    print('\n\n1 - Adicionar pessoa\n2 - Buscar pessoa\n3 - Listar nomes\n4 - Listar Cidades Unicas\n5 - Sair')


lista = []
while True:
    menu()
    opcao = int(input('Digite a opção desejada: '))
    if opcao == 1:
        lista.append((adicionar_pessoa()))
        os.system('cls')
    elif opcao == 2:
        print(buscar_cpf(input('Digite o CPF para pesquisa: ')) + '\n\n')
    elif opcao == 3:
        print(listar_nomes())
        time.sleep(4)
        os.system('cls')
    elif opcao == 4:
        print(listar_cidades())
        time.sleep(4)
        os.system('cls')
    elif opcao == 5:
        break
    else:
        print('Opção inválida')
        time.sleep(4)
        os.system('cls')
