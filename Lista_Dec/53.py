n = int(input())

for x in range(n):
    jogador1, jogador2 = input().split()

    if jogador1 == "pedra":
        if jogador2 == "tesoura":
            print("Jogador 01 venceu.")
        elif jogador2 == "papel":
            print("Jogador 02 venceu.")
        else:
            print("Empate.")
    elif jogador1 == "papel":
        if jogador2 == "pedra":
            print("Jogador 01 venceu.")
        elif jogador2 == "tesoura":
            print("Jogador 02 venceu.")
        else:
            print("Empate.")
    elif jogador1 == "tesoura":
        if jogador2 == "papel":
            print("Jogador 01 venceu.")
        elif jogador2 == "pedra":
            print("Jogador 02 venceu.")
        else:
            print("Empate.")
