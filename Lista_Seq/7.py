def realidade(a, b, c):
    if ((int(b) ** 2) - 4 * int(a) * int(c)) >= 0:
        return print("reais")
    else:
        return print("complexas")


# main
x, y, z = input().split()
realidade(x, y, z)
