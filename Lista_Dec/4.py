problems = int(input())
solucions, contagem_certeza = int(0), int(0)

for x in range(problems):
    leakim, sarev, odranoel = map(int, (input().split()))
    contagem_certezas = leakim + sarev + odranoel
    if contagem_certezas >= 2:
        solucions += 1
print(solucions)
