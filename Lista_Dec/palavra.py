palavra = input()
minuscula = 0

for letra in palavra:
    if letra.islower():
        minuscula += 1


maiuscula = len(palavra) - minuscula

if minuscula > maiuscula:
    print(palavra.lower())
elif maiuscula > minuscula:
    print(palavra.upper())
else:
    print(palavra.lower())
