#  implementar média aritmética
#  calcular a quantidade de horas a partir do resultado da media


def pratos(a):
    pratos = int(a)
    if pratos < 0:
        return 0
    # print(qtd_precisa)

    melhor_caso = (pratos * 5) / 60
    pior_caso = (pratos * 15) / 60

    return print("Entre {} e {}.".format("%0.2f" % melhor_caso, "%0.2f" % pior_caso))


# main

prato = int(input())
pratos(prato)
