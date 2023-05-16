# vestimenta = um par de botas e um chápeu


def vestimentas(x, y):
    botas, chapeus = int(x), int(y)
    # condicionais
    if botas <= 0 or botas >= 111:
        return
    if chapeus <= 0 or chapeus >= 111:
        return
    # adicionando a qtd de botas definidas por um par
    pares_botas = botas * 2
    qtd_vestimentas = int()
    # print(pares_botas)

    if chapeus >= 1:
        if pares_botas >= 2:
            while pares_botas > 0 and chapeus > 0:
                qtd_vestimentas += 1
                chapeus -= 1
                pares_botas -= 2

    return print(qtd_vestimentas * 2)


# main
pares_botas, chapeus = input().split()
vestimentas(pares_botas, chapeus)
