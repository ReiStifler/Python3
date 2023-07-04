numbers = input()
lista = numbers.split(" ")

lista = list(map(int, lista))


menor = min(lista)
maior = max(lista)

posicaoMenor = lista.index(menor)
posicaoMaior = lista.index(maior)

print(f"{menor} {posicaoMenor}")
print(f"{maior} {posicaoMaior}")

n = len(lista)
contador = 1

listaParaImprimir = f"{lista[0]}"

while contador < n:
    listaParaImprimir += f" {lista[contador]}"

    contador += 1

print(listaParaImprimir)
