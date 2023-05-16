# vestimenta = um par de botas e um chápeu


def vestimentas(x, y):
    botas, chapeus = int(x), int(y)
    vestimentas = int()
    # condicionais
    if botas <= 0 or botas >= 111:
        return
    if chapeus <= 0 or chapeus >= 111:
        return
    # adicionando a qtd de botas definidas por um par
    botas = botas * 2

    if chapeus >= 1:
        if botas >= 2:
            while chapeus >= 1  botas >= 2:
                vestimentas += 1
                chapeus -= 1
                botas -= 2
    return print(vestimentas)


# main
pares_botas, chapeus = input().split()
vestimentas(pares_botas, chapeus)
