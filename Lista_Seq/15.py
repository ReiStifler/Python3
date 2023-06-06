def piscininha(x, y, w, h, a, b):
    calcula_area = int(w) * int(h)
    return


def piscininha(x, y, w, h, a, b):
    if x <= a <= x + w and y <= b <= y + h:
        print("Dando um tchibum")
    elif (a == x or a == x + w) and y <= b <= y + h:
        print("So com os pezin dentro da agua")
    elif (b == y or b == y + h) and x <= a <= x + w:
        print("So com os pezin dentro da agua")
    else:
        print("Tomando um solzin")
