# def verifica_letras():
#     contadora = int()
#     for i in range(len(palavra)):
#         if "A" or "C" or "G" or "T" == palavra[i]:
#             contadora += 1
#     if contadora >= 4:
#         return print("Segredos desvendados")
#     else:
#         return print("Feiticeiro misterioso")


# # main

# qtd_letras = int()
# newplw = ""
# for i in range(qtd_letras):
#     newplw += input(i)

# print(newplw)


n = int(input())
s = input()
m = n / 4

A = s.count("A")
C = s.count("C")
G = s.count("G")
T = s.count("T")

if A <= m and C <= m and G <= m and T <= m:
    genoma = ""
    for nucleotide in s:
        if nucleotide == "?":
            if A < m:
                genoma += "A"
                A += 1
            elif C < m:
                genoma += "C"
                C += 1
            elif G < m:
                genoma += "G"
                G += 1
            else:
                genoma += "T"
                T += 1
        else:
            genoma += nucleotide
    if A == C == G == T == m:
        print("Segredos desvendados")
    else:
        print("Feiticeiro misterioso")
else:
    print("Feiticeiro misterioso")
