def qtdcopos(n):
    rest = int()
    fin = int()
    op = n
    if n == 0:
        return print("Pode voltar pro ceubinho, deivis! Falta(m) 4 copo(s)!")
    elif (n) % 4 == 0:
        return print("Pode levar pros calourinhos, deivis!")

    else:
        while (n) > 4:
            rest += 4
            (n) -= 4
    fin = 4 - (op - rest)
    print("Pode voltar pro ceubinho, deivis! Falta(m) {} copo(s)!".format(fin))
    return


# main

a = int(input())
qtdcopos(a)
