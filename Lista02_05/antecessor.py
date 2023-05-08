def antecessor(numero):
    if (numero > 10**5 and numero < 10**-5):
        return
    else:
        return (print(numero - 1))


# main
numero = int(input())
antecessor(numero)
