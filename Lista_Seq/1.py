def area(a, b, c):
    # recendo e convertendo as medidas
    md1 = int(a)
    md2 = int(b)
    fig = c
    losango = int((md1 * md2) / 2)
    retang = md1 * md2

    if fig == "losango":
        return print("O losango tem {} de area".format(losango))
    elif fig == "retangulo":
        return print("O retangulo tem {} de area".format(retang))


# main

medida1, medida2, figura = input().split()
area(medida1, medida2, figura)
