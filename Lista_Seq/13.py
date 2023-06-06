def sedeDeMelancia(a):
    # Utilizando O Resultado Da Divisão, Verifica Se O Valor É Par Ou Impar

    operador = int(a) / 2

    if operador % 2 == 0:
        print("SIM")
    else:
        print("NAO")


# main

q = input()
sedeDeMelancia(q)
