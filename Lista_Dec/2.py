poluA, poluB, cresA, cresB = map(float, (input().split()))

contadoryears = int()

if cresB > cresA:
    print("A nunca alcancara B.")

else:
    while poluA < poluB and contadoryears <= 1000:
        poluA += int(poluA * (cresA / 100))
        poluB += int(poluB * (cresB / 100))
        contadoryears += 1
    if contadoryears < 1000:
        print("Vai alcancar em {} ano(s).".format(contadoryears))
    else:
        print("Mais de um milenio.")
