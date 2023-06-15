qtd_cidadao = int(input())
total_dinheiros, contador = int(), qtd_cidadao

while contador > 0:
    dinheiros = int(input())
    if dinheiros < 1000:
        total_dinheiros += 1000 - dinheiros
    contador -= 1
print(total_dinheiros)
