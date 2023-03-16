# Description: A Entidade ganhou vários blocos de encaixar, mas infelizmente, os blocos só se encaixam quando têm exatamente o mesmo tamanho. Ela quer encaixar os blocos de forma que consiga a menor quantidade de torres possível. Faça um programa que preveja o tamanho da maior torre e a quantidade de torres no final.
# Entrada: A primeira linha da entrada terá um inteiro n (1 <= n <= 1000) indicando a quantidade de blocos a Entidade ganhou. Na linha seguinte, terão n inteiros h_i  (1 <= h_i <= 1000), representando o tamanho do i-ésima bloco.
# Saida: A saída deverá conter dois inteiros t e k, representando respecitvamente o tamanho da maior torre e quantas torres ficaram no final.

n = int(input())  # numero de blocos

input = input().split()  # separa em uma lista
inputs = [int(i) for i in input]  # transforma em inteiros

k = len(set(inputs))  # quantidade de torres
t = 0

for number in inputs:
    if inputs.count(number) > t:  # quantiadde de repeticoes de cada digito
        t = inputs.count(number)

print(t, k)
