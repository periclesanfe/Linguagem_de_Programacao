# description: Escreva um programa para ler as resposta de uma turma em uma prova com 5 questões e, a partir do gabarito fornecido ao final, obter a maior nota, a menor nota e a média das notas da turma.
# O programa deve receber os dados das respostas dos alunos (Primeiro Nome e Respostas). O primeiro nome e as respostas às 5 questões são informadas na mesma linha e separadas por um espaço em branco. A leitura dos dados dos alunos se encerra quando é encontrado o caractere *. Na linha seguinte é fornecido o gabarito das 5 questões.
# A saída consiste de 3 linhas contendo, respectivamente: a maior nota (de 0 a 5), a menor menor nota (de 0 a 5) e a média das notas da turma (0.00 a 5.00). Observe que a média possui 2 casas decimais.

def calcular_nota(aluno, gabarito):
    nota = 0
    for i in range(5):
        if aluno[i] == gabarito[i]:
            nota += 1
    return nota


alunos = {}
maior_nota = 0
menor_nota = 5
media = 0.00
resposta = ''

while True:
    entrada = input().split()
    if entrada[0] == '*':
        resposta = input()
        for i in alunos.values():
            nota = calcular_nota(i, resposta)
            if nota > maior_nota:
                maior_nota = nota
            if nota < menor_nota:
                menor_nota = nota
            media += nota
        media = media / float(len(alunos))
        print(f'Maior: {maior_nota}\nMenor: {menor_nota}\nMedia: {media:.2f}')
        break
    else:
        alunos[entrada[0]] = entrada[1]
