def soma_prefixos(vetor):
    soma = 0
    prefixos = []

    for valor in vetor:
        soma += valor
        prefixos.append(soma)

    return prefixos


vetor = list(map(int, input().split()))
prefixos = soma_prefixos(vetor)
print(" ".join(map(str, prefixos)))
print(" ".join(map(str, vetor)))
