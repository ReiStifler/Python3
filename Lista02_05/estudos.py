#  implementar média aritmética
#  calcular a quantidade de horas a partir do resultado da media


def estudo(a):
    nota = int(a)
    qtd_precisa = 10 - nota
    if nota < 0:
        return 0
    #print(qtd_precisa)

    melhor_caso = qtd_precisa * 3
    pior_caso = qtd_precisa * 5

    if nota > 10:
        melhor_caso = 0
        pior_caso = 0
        return print("Entre {} e {}.".format(melhor_caso, pior_caso))

    return print("Entre {} e {}.".format(melhor_caso, pior_caso))


# main

nota = int(input())
estudo(nota)
