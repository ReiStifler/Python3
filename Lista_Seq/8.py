def formamisteriosa(a, b, c):
    if int(a) == int(b):  # or int(b) == int(c) or int(a) == int(c):
        print("pode ser quadrado")
    else:
        print("pode ser retangulo")
    if (
        int(a) + int(b) > int(c)
        and int(b) + int(c) > int(a)
        and int(a) + int(c) > int(b)
    ):
        if int(a) == int(b) and int(b) == int(c):
            print("pode ser triangulo equilatero")
        elif int(a) != int(b) and int(b) != int(c) and int(a) != int(c):
            print("pode ser triangulo escaleno")
        if (
            int(a) == int(b)
            and int(a) != int(c)
            or int(a) == int(c)
            and int(a) != int(b)
        ):
            print("pode ser triangulo isosceles")


# main

a, b, c = input().split()
formamisteriosa(a, b, c)
