def atualizaMatriz(matriz, lin, col, tipo):
    matriz[lin][col] = tipo

    return matriz


def imprimeJogo(matriz):
    l1 = matriz[0]
    l2 = matriz[1]
    l3 = matriz[2]

    def imprimirSTR(linha):
        linhaSTR = ""

        for i in linha:
            linhaSTR += f"{i}"

        print(linhaSTR)

    imprimirSTR(l1)
    imprimirSTR(l2)
    imprimirSTR(l3)
