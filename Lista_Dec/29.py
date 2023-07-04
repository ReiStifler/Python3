def jogoTerminou(matriz):
    l1 = matriz[0]
    l2 = matriz[1]
    l3 = matriz[2]

    if l1 == l2 and l2 == l3 and l3 == l1:
        estado_partida = 0
    else:
        if l1[0] == l1[1] and l1[0] == l1[2] and l1[1] == l1[2]:
            estado_partida = 1
        elif l2[0] == l2[1] and l2[0] == l2[2] and l2[1] == l2[2]:
            estado_partida = 1
        elif l3[0] == l3[1] and l3[0] == l3[2] and l3[1] == l3[2]:
            estado_partida = 1
        elif l1[0] == l2[1] and l1[0] == l3[2] and l2[1] == l3[2]:
            estado_partida = 1
        elif l1[2] == l2[1] and l1[2] == l3[0] and l2[1] == l3[0]:
            estado_partida = 1
        elif l1[0] == l2[0] and l1[0] == l3[0] and l2[0] == l3[0]:
            estado_partida = 1
        elif l1[1] == l2[1] and l1[1] == l3[1] and l2[1] == l3[1]:
            estado_partida = 1
        elif l1[2] == l2[2] and l1[2] == l3[2] and l2[2] == l3[2]:
            estado_partida = 1
        else:
            estado_partida = 2

    return estado_partida
