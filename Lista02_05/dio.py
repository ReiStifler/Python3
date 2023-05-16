def quantosSemestres(m, a, s):
    m, a, s = int(m), int(a), int(s)
    dig = m // 100000
    ano_ingresso = (m // 10000000) + 2000
    anos_totais = a - ano_ingresso
    semestre_ingresso = dig % 10
    semestre_total = anos_totais * 2

    if a < ano_ingresso:
        if s < semestre_ingresso:
            return
    if anos_totais == 0:
        if s == semestre_ingresso:
            semestre_total = 0
        else:
            semestre_total = anos_totais + 1
    else:
        if s == semestre_ingresso:
            semestre_total = anos_totais * 2
        else:
            semestre_total = (anos_totais * 2) - 1

    return print(semestre_total)


test, test1, test2 = input().split(",")
quantosSemestres(test, test1, test2)
