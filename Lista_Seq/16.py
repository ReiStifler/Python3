# para contar como uma pessoa jantando, a quantidade de garfos e facas devem ser iguais, 1 colher contra como uma pessoa jantando


def quantosJantam(convidades, garfo, faca, colher):
    Jantam = int()
    while garfo > 0 and faca > 0:
        if convidades == 0:
            return print(Jantam)
        convidades -= 1
        garfo -= 1
        faca -= 1
        Jantam += 1
    while colher > 0:
        if convidades == 0:
            return print(Jantam)
        convidades -= 1
        colher -= 1
        Jantam += 1
    return print(Jantam)


# main

n, g, f, c = [int(x) for x in range(4)]
quantosJantam(12, 0, 1, 7)
