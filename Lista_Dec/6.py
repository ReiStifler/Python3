contador = int(input())
elefante = int(1)

while contador != 0:
    if elefante == 1:
        print("{} elefante incomoda muita gente...".format(elefante))
    else:
        print("{} elefantes incomodam muita gente...".format(elefante))
    elefante += 1
    incomoda = str("incomodam, ") * (elefante - 1)
    incomoda2 = str("incomodam")
    if elefante > 1:
        print("{} elefantes {}{} muito mais...".format(elefante, incomoda, incomoda2))
    contador -= 1
