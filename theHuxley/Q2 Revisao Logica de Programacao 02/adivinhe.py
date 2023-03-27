# description: Trata-se de um jogo de lógica cujo seu objetivo como jogador é descobrir a senha secreta escolhida por um oponente. A senha a ser descoberta é formada por uma seqüência de caracteres de algum alfabeto. Para descobrir qual foi a senha, você "chuta" uma provável senha para o seu oponente. O chute é uma sequência de caracteres com o mesmo número de caracteres da senha. E os caracteres devem pertencer ao mesmo alfabeto.
# Após cada chute seu, você receberá uma resposta, que consiste de 2 inteiros (E,B) indicando o quão bom foi o seu chute. Se um caractere do chute existe na senha na mesma posição (da string), então ele conta como "excelente" (E). Caso contrário, se o caractere existe na senha, mas em uma posição diferente, ele conta como "bom" (B). Um dado caractere do chute não é contado duas vezes (ou seja, se ele foi contado como excelente, não é contado como bom). A tabela abaixo ilustra o jogo com alguns exemplos
# Baseado nas respostas recebidas, o jogador pode deduzir qual foi a senha escolhida pelo oponente. O objetivo do jogo é encontrar a senha com o número mínimo de chutes.
# Já o seu objetivo é um pouco mais simples: escrever um programa que receba a senha do primeiro jogador e em seguida recebe os chutes do segundo jogador. Você deve fornecer as respostas de acordo com o explicado acima.
# A primeira linha da entrada consiste de um número K representando o número de jogos que serão realizados. A próxima linha consiste de um número N, [0 < N < 8], representando o tamanho da senha a ser utilizada no próximo jogo. A próxima linha contém uma senha contendo dígitos, entre 1 e 7, com exatamente N caracteres que será utilizada no jogo em questão.
# As próximas linhas contêm os chutes dados pelo segundo jogador e, portanto, consistem de uma sequência de dígitos, entre 1 e 7, com exatamente N caracteres. Cada jogo termina quando a senha é acertada ou quando o jogador desiste de tentar digitando uma seqüência de N caracteres '0'. Após cada jogo, o próximo jogo tem inicio a partir da leitura de uma linha contendo um inteiro indicando o tamanho da próxima senha. Na linha seguinte é dada a nova senha e o jogo prossegue com os chutes.
# Para cada chute, seu programa deve imprimir (E,B), correspondendo ao número de excelentes e bons respectivamente.

def contar_excelente(chute, senha):
    E = 0
    for i in range(len(chute)):
        if chute[i] == senha[i]:
            E += 1
    return E


def contar_otimo(chute, senha):
    B = 0
    lista_sem_repeticao = set(chute)
    for item in lista_sem_repeticao:
        if item in senha:
            if chute.index(item) != senha.index(item):
                B += 1
    return B


K = input()

for i in range(0, int(K)):
    N = input()
    senha = input()

    while True:
        E, B = 0, 0
        chute = input()
        if chute == ('0' * int(N)):
            break
        elif chute == senha:
            E = len(chute)
            print(f'({E},{B})')
            break
        else:
            E = contar_excelente(chute, senha)
            B = contar_otimo(chute, senha)
        print(f'({E},{B})')
