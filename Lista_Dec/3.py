qtd_amigos, ingresso_price = map(int, (input().split()))
total_dinheiros = int()
for x in range(qtd_amigos):
    dinheiros = int(input())
    total_dinheiros += dinheiros / qtd_amigos
if total_dinheiros >= ingresso_price:
    print("media: {}".format(int(total_dinheiros)))
    print("o rock reinara mais uma vez")
else:
    print("media: {}".format(int(total_dinheiros)))
    print("rockeiros trabalhando ja")
