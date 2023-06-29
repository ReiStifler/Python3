def calcula_nota(a, b, c):
    if (float(a + b + c)) / 3 >= 7:
        print("O ALUNO {} FOI APROVADO".format(x))
    else:
        print("O ALUNO {} FOI REPROVADO".format(x))


alunos = int(input())

for x in range(alunos):
    notes1, notes2, notes3 = map(float, (input().split()))
    calcula_nota(notes1, notes2, notes3)
