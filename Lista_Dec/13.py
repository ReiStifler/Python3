soma_inversos = 0
contador = 0

while True:
    valor = int(input())
    if valor == -1:
        break
    soma_inversos += 1 / valor
    contador += 1

media_harmonica = contador / soma_inversos

print(int(media_harmonica))
