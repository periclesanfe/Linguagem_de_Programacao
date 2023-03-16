# description: Faça um programa que receba os elementos de 2 vetores e imprima na saída a união, a interseção e a diferença entre os 2 vetores.
# Você deve usar apenas arrays unidimensionais (em python, apenas listas) e deve evitar uso de funções embutidas.
# Sugiro o uso apenas dos operadores "in" e "not in" para verificar se um item está ou não em uma lista e da função "append()" para incluir o elemento na lista. Pode também usar a função "copy() para copiar os elementos da lista."

n_vet1, n_vet2 = int(input()), int(input())
vet1, vet2 = [], []

for i in range(n_vet1):
    vet1.append(input())
for i in range(n_vet2):
    vet2.append(input())

uniao = []
for i in range(n_vet2):
    if vet2[i] not in uniao:
        uniao.append(vet2[i])
for i in range(n_vet1):
    if vet1[i] not in uniao:
        uniao.append(vet1[i])


intersec = []
for i in range(n_vet1):
    if vet1[i] in vet2:
        intersec.append(vet1[i])

diff = []
for i in range(n_vet1):
    if vet1[i] not in vet2:
        diff.append(vet1[i])


print(uniao)
print(intersec)
print(diff)
