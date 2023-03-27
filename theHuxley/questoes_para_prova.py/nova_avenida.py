N, M = input().split()
ruas = []
valor_mais_baixo = 0
for i in range(int(N)):
    ruas.append(input().split())

for i in range(int(M)):
    total = 0
    for j in range(int(N)):
        total += int(ruas[j][i])
    if i == 0:
        valor_mais_baixo = total
    if total < valor_mais_baixo:
        valor_mais_baixo = total

print(valor_mais_baixo)
