# description: Periodicamente as crianças brasileiras devem tomar vacinas que as protegem de diversas doenças. Escrever um programa para ler o ano em que a criança toma a 1a dose e a periodicidade (intervalo em anos) da vacina e exibir em que outros anos a criança deve tomar as próximas doses desta vacina, sabendo que são 4(quatro) doses ao total.

first_dose = int(input())
frequency = int(input())

output = []
for i in range(3):
    first_dose += frequency
    output.append(first_dose)
print(*output, sep=' ')
