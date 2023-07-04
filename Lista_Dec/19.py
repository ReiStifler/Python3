sequencia = list(map(int, input().strip().split()))
n = len(sequencia)
inversoes = 0

for i in range(n):
    for j in range(i + 1, n):
        if sequencia[j] < sequencia[i]:
            inversoes += 1

print(inversoes)
