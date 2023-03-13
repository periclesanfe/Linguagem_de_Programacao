# Escreva um programa que leia uma nota de 0 a 10 de um aluno, se a nota for maior ou igual a 7 ele esta aprovado, se for menor que 7 e maior ou igual a 4 ele esta de recuperação, se for menor que 4 ele esta reprovado.
# Se ele estiver de recuperação, pedir a nota da recuperação, se a nota da recuperação for maior ou igual a 5 ele esta aprovado na final, se for menor que 5 ele esta reprovado.

def media(nota):
    if nota >= 7:
        return "Aprovado"
    elif nota < 7 and nota >= 4:
        nota_rec = float(input("Digite a nota da recuperação: "))
        if nota_rec >= 5:
            return "Aprovado na final"
        else:
            return "Reprovado na final"
    else:
        return 'Reprovado'


nota = float(input("Digite a nota do aluno: "))
print(media(nota))
