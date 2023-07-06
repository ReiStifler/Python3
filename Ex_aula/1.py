def calculaPrecoCasa(
    bairro, escola, metragem, quartos, banheiros, piscina_tem, tam_piscina
):
    precoCasaFinal = float()

    # Valor Da Csa Em Relação Ao Bairro

    if bairro == "A":
        precoCasaFinal = 100000
    elif bairro == "B":
        precoCasaFinal = 150000
    elif bairro == "C":
        precoCasaFinal = 200000
    else:
        return print("ERROR - 500")

    # Valor Da Csa Em Relação A Nota Da Escola

    if int(escola) > 8:
        precoCasaFinal *= 1.1
    elif int(escola) >= 6 and int(escola) < 8:
        precoCasaFinal
    elif int(escola) < 6:
        precoCasaFinal *= 0.9

    # Valor Da Csa Em Relação A Metragem

    if int(metragem) > 100:
        int(metragem) - 100
        precoCasaFinal += 1000 * (int(metragem) / 40)

        # while int(metragem) > 40:
        #     precoCasaFinal += 1000
        #     int(metragem - 40)

    # Valor Da Csa Em Relação Ao Qtd De Quartos

    if int(quartos) > 1:
        precoCasaFinal *= 1.1 * int(quartos)

    # Valor Da Csa Em Relação A Qtd De Banheiros

    if int(banheiros) > 1:
        if int(quartos) > int(banheiros):
            Engenheiro = int(quartos) - int(banheiros)
            precoCasaFinal *= 0.65 * Engenheiro

    # Valor Da Csa Em Relação A Existência De Uma Piscina E Seu Tamanho
    if int(piscina_tem) >= 1:
        if int(tam_piscina) < 100:
            precoCasaFinal *= 0.95

    return print("%.2f" % precoCasaFinal)


# main

a, b, c, d, e, f, g = input().split()
calculaPrecoCasa(a, b, c, d, e, f, g)
