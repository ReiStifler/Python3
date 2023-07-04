def maior_norma(vetor1, vetor2):
    norma1 = sum(abs(x) for x in vetor1)
    norma2 = sum(abs(x) for x in vetor2)

    if norma1 > norma2:
        print("PRIMEIRO")
    else:
        print("SEGUNDO")
