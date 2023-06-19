number1, number2 = map(int, (input().split()))
if number1 < number2:
    verificador = number2
else:
    verificador = number1


while verificador > 0:
    if number1 % verificador == 0 and number2 % verificador == 0:
        if True and verificador == 1:
            print("Sao co-primos.")
            break
        else:
            print("Nao sao co-primos!")
            break
    verificador -= 1
