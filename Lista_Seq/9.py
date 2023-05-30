def classificador(a, b, c):
    if (
        int(a) + int(b) > int(c)
        and int(b) + int(c) > int(a)
        and int(a) + int(c) > int(b)
    ):
        print("triangulo")
        if int(a) == int(b) or int(a) == int(c) or int(b) == int(c):
            print("isosceles")
        if int(a) != int(b) and int(a) != int(c) and int(b) != int(c):
            print("escaleno")
        if int(a) == int(b) and int(a) == int(c) and int(b) == int(c):
            print("equilatero")
        if (
            int(a) + int(b) == int(c) ** 2
            or int(a) + int(c) == int(b) ** 2
            or int(b) + int(c) == int(a) ** 2
        ):
            print("retangulo")
    else:
        return print("gondim sendo gondim")


# main

w, e, r = input().split()
classificador(w, e, r)
