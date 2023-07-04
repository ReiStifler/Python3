pontuacoes = []
entrada = input()
valores = entrada.split()
for valor in valores:
    pontuacao = int(valor)
    if pontuacao < 0:
        break
    pontuacoes.append(pontuacao)
print(*pontuacoes[::-1])
