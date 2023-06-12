cot_dolar, tam_lote, qtd_lotes = map(float, (input().split()))
venda = (cot_dolar * 1.025) * tam_lote
contador = int()
while qtd_lotes > 0:
    contador += 1
    print("Lote: {} - Total da venda: R$ {}".format(contador, "%.2f" % venda))
    qtd_lotes -= 1
