def EhRetangulo(a, b, c):
    if (
        a**2 + b**2 == c**2
        or b**2 + c**2 == a**2
        or a**2 + c**2 == b**2
    ):
        return 1
    else:
        return 0


# main

e, r, t = [int(x) for x in range(3)]
EhRetangulo(3, 4, 5)
