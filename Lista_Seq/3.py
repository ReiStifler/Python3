def area(a, b, c):
    # recendo e convertendo as medidas
    losango = (int(a) * int(b)) / 2
    retang = int(a) * int(b)
    triang = (int(a) * int(b)) / 2
    circo = (int(a) ** 2) * 3

    if c == "losango":
        return print("O losango tem {} de area".format(int(losango)))
    elif c == "retangulo":
        return print("O retangulo tem {} de area".format(retang))
    elif c == "triangulo":
        return print("O triangulo tem {} de area".format(int(triang)))
    elif c == "circulo":
        return print("O circulo tem {} de area".format(circo))


# main

medida1, medida2, figura = input().split()
area(medida1, medida2, figura)
