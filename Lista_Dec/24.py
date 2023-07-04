nums = input()
lista = nums.split(" ")
lista = list(map(int, lista))

somaX = 0
nTermos = 0

for i in lista:
    somaX += i
    nTermos += 1

mediaX = somaX / nTermos

medias2 = 0

for i in lista:
    dif = mediaX - i
    dif = dif**2
    medias2 += dif

variancia = medias2 / nTermos
desvio = variancia ** (1 / 2)

print(f"{variancia:.1f}")
print(f"{desvio:.1f}")
