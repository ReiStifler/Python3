def ComoVaiSuaSaude(Peso, Sex, Altura):
    if Sex == "H":
        Fat = 72.7 * float(Altura) - 58
    elif Sex == "M":
        Fat = 62.1 * float(Altura) - 44.7
    else:
        return print("Invalid Gen")

    IMC = float(Peso) / float(Altura) ** 2

    diference = float(Peso) - Fat

    percentual_diference = (diference / Fat) * 100

    print(float(Peso))
    print(IMC)
    print(Fat)
    print(percentual_diference)
    print("PI = {}".format(float(Peso) - Fat))
    print("P_Dif = {}".format(Fat * 0.05))
    print("P_Dif2 = {}".format(Fat * 0.1))

    if diference > 0:
        if abs(float(Peso) - Fat) < 0.05 * Fat and IMC >= 18.5 and IMC < 25:
            print("Você tem uma saúde ótima!")

        elif float(Peso) - Fat <= 10 and IMC >= 18.5 and IMC < 25:
            print("Você tem uma saúde boa.")

        elif float(Peso) < Fat and IMC < 18.5:
            print("Atenção: Fique atento ao baixo peso!")

        elif float(Peso) - Fat > 10 and IMC >= 25 and IMC < 30:
            print("Cuidado: Medidas acima do padrão!")

        elif float(Peso) - Fat > 10 and IMC >= 30:
            print("Procure Ajuda: Excesso de medidas!")

        else:
            print("Sem apontamento.")

    else:
        print("Sem apontamento.")


# main
# a,b,c = [float(x) for x in range(3)]
a, b, c = input().split()
ComoVaiSuaSaude(a, b, c)
