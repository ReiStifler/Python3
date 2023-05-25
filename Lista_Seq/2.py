def area(a, b, c):
    # recendo e convertendo as medidas
    losango = (int(a) * int(b)) / 2
    retang = int(a) * int(b)
    triang = (int(a) * int(b)) / 2

    if c == "losango":
        return print("O losango tem {} de area".format(int(losango)))
    if c == "retangulo":
        return print("O retangulo tem {} de area".format(retang))
    if c == "triangulo":
        return print("O triangulo tem {} de area".format(int(triang)))


# main

medida1, medida2, figura = input().split()
area(medida1, medida2, figura)
