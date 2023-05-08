def print_rectangle(a, b, c):
    # passando os tamanhos para inteiros

    tam1, tam2, tam3 = int(a), int(b), int(c)

    # Manipulação para determinar quantos espaços entre o primeiro e o ultimo caracter

    tam_x1, tam_x2, tam_x3 = tam1 - 2, tam2 - 2, tam3 - 2

    # validando as entradas dos tamanhos para tamanho >=4

    if tam1 <= 3 and tam2 <= 3 and tam3 <= 3:
        return

    # lógica da função

    qtd_x = str("x" * tam1)
    print(tam1)
    print(qtd_x[:tam1:])
    print(qtd_x[0] + str((" " * tam_x1)) + qtd_x[-1])
    print(qtd_x[0] + str((" " * tam_x1)) + qtd_x[-1])
    print(qtd_x[:tam1:])

    qtd_x = str("x" * tam2)
    print(tam2)
    print(qtd_x[:tam2:])
    print(qtd_x[0] + str((" " * tam_x2)) + qtd_x[-1])
    print(qtd_x[0] + str((" " * tam_x2)) + qtd_x[-1])
    print(qtd_x[:tam2:])

    qtd_x = str("x" * tam3)
    print(tam3)
    print(qtd_x[:tam3:])
    print(qtd_x[0] + str((" " * tam_x3)) + qtd_x[-1])
    print(qtd_x[0] + str((" " * tam_x3)) + qtd_x[-1])
    print(qtd_x[:tam3:])


# main
a, b, c = input().split()
print_rectangle(a, b, c)
