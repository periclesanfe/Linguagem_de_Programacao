# Description: A Entidade ganhou vários blocos de encaixar, mas infelizmente, os blocos só se encaixam quando têm exatamente o mesmo tamanho. Ela quer encaixar os blocos de forma que consiga a menor quantidade de torres possível. Faça um programa que preveja o tamanho da maior torre e a quantidade de torres no final.
# Entrada: A primeira linha da entrada terá um inteiro n (1 <= n <= 1000) indicando a quantidade de blocos a Entidade ganhou. Na linha seguinte, terão n inteiros h_i  (1 <= h_i <= 1000), representando o tamanho do i-ésima bloco.
# Saida: A saída deverá conter dois inteiros t e k, representando respecitvamente o tamanho da maior torre e quantas torres ficaram no final.

n = int(input())
# use a poha do count() pra contar quantas vezes um elemento aparece na lista
inputs = []


for i in range(0, n + 1):
    inputs.append(int(input()))

contador = Counter(inputs)
