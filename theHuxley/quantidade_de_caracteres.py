# Description: Crie um programa que tenha uma única função, além da principal, que receberá como parâmetro uma string não vazia s (com no máximo 50 caracteres de conteúdo) e exibirá a quantidade de caracteres de s. Observações: (a) apenas um laço de repetição; (b) sem matrizes auxiliares; (c) não usar funções prontas; (d) função iterativa.

while True:
    try:
        s = input()
        if len(s) > 50:
            raise ValueError
    except ValueError:
        print('String deve ter no máximo 50 caracteres.')
        continue
    print(len(s))
    break
