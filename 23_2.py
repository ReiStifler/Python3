# def ComoVaiSuaSaude(peso, sexo, altura):
#     if sexo == "M":
#         PI = (72.7 * altura) - 58
#     elif sexo == "F":
#         PI = (62.1 * altura) - 44.7
#     else:
#         return "Sem apontamento."

#     IMC = peso / (altura * altura)

#     if IMC < 18.5:
#         if peso < PI:
#             return "Atenção: Fique atento ao baixo peso!"
#         else:
#             return "Cuidado: Medidas acima do padrão!"
#     elif IMC < 25:
#         if abs(peso - PI) <= 0.05 * PI:
#             return "Você tem uma saúde ótima!"
#         elif abs(peso - PI) <= 0.1 * PI:
#             return "Você tem uma saúde boa."
#         else:
#             return "Cuidado: Medidas acima do padrão!"
#     elif IMC < 30:
#         if abs(peso - PI) > 0.1 * PI:
#             return "Cuidado: Medidas acima do padrão!"
#     elif abs(peso - PI) > 0.1 * PI:
#         return "Procure Ajuda: Excesso de medidas!"
#     else:
#         return "Sem apontamento."


def ComoVaiSuaSaude(peso, sexo, altura):
    if sexo == "M":
        PI = (72.7 * altura) - 58
    elif sexo == "F":
        PI = (62.1 * altura) - 44.7
    else:
        return "Sem apontamento."

    IMC = peso / (altura * altura)

    # print(PI)
    # print(IMC)
    # print(abs((peso - PI)))
    # print(0.05 * PI)
    # print(0.1 * PI)

    if IMC < 18.5:
        if peso < PI:
            return "Atenção: Fique atento ao baixo peso!"
        else:
            return "Cuidado: Medidas acima do padrão!"
    elif 18.5 < IMC < 25:
        if abs(peso - PI) <= 0.05 * PI:
            return "Você tem uma saúde ótima!"
        elif abs(peso - PI) <= 0.1 * PI:
            return "Você tem uma saúde boa."
    elif 25 <= IMC < 30:
        if abs(peso - PI) > 0.1 * PI:
            return "Cuidado: Medidas acima do padrão!"
    elif IMC >= 30:
        if abs(peso - PI) > 0.1 * PI:
            return "Procure Ajuda: Excesso de medidas!"
    return "Sem apontamento."


# main
print(ComoVaiSuaSaude(72, "M", 1.92))
