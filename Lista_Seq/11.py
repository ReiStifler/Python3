def riscu(powerA, powerB):
    if int(powerA) > int(powerB):
        return print("Jogador A vence")
    elif int(powerA) < int(powerB):
        return print("Jogador B vence")
    if int(powerA) == int(powerB):
        return print("Dois jogadores igualmente fracos")
