def qualPeriodo(m, a, s):
    matricula, ano_atual, semestre_atual = int(m), int(a), int(s)

    # verificação de entradas OK

    if matricula <= 100000000 or matricula >= 500000000:
        return 0
    else:
        if ano_atual >= 2050 or ano_atual <= 2010:
            return 0
        else:
            if semestre_atual != 0 and semestre_atual != 1:
                return 0

    #   pegando os valores de entrada e do ano atual

    ano_entrada = str(matricula)[:2]
    semestre_entrada = str(matricula)[3:4]
    ano_entrada = str(20) + ano_entrada

    # manipulações para pegar valores em string e depois retornar uma entrada

    ano_entrada = int(ano_entrada)
    semestre_entrada = int(semestre_entrada)
    qtd_semestres = int()
    qtd_anos = ano_atual - ano_entrada

    # calcular a quantidade de semestres utilizando a quatidade de anos e a igualdade entre os semestres

    if (ano_atual < ano_entrada):
        if (semestre_atual < semestre_entrada):
            return
        return
    if (qtd_anos == 0):
        if (semestre_atual == semestre_entrada):
            qtd_semestres = 1
        else:
            if (semestre_atual == 1 and semestre_entrada == 1):
                qtd_semestres = qtd_semestres + 3
            else:
                qtd_semestres = 2
    else:
        if (semestre_atual == 1 and semestre_entrada == 1):
            qtd_semestres = (qtd_anos*2) + 1
        else:
            qtd_semestres = (qtd_anos*2)

    print(qtd_semestres)


# main
test, test1, test2 = input().split(",")
qualPeriodo(test, test1, test2)
