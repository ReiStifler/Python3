number = int(input())
contador = int(1)

while contador <= number:
    if contador % 3 == 0 and contador % 5 == 0:
        print("Fizz Buzz")

    elif contador % 3 == 0:
        print("Fizz")

    elif contador % 5 == 0:
        print("Buzz")

    else:
        print(contador)
    contador += 1
