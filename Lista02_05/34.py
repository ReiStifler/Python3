def concatenar(a, b):
    return print(a + b)


def repetir(a, c):
    return print(a * int(c))


def ambos(a, b, c):
    return print((a + b) * int(c))


# main
palavra1, palavra2, number = input().split()
concatenar(palavra1, palavra2)
repetir(palavra1, number)
ambos(palavra1, palavra2, number)
