def Alfabeto(simbolo):
    vogais = ["a", "e", "i", "o", "u"]

    if simbolo.isalpha():
        if simbolo.lower() in vogais:
            return print("Vogal")
        else:
            return print("Consoante")
    else:
        return print("Não está no alfabeto")


# main

sim = input()
Alfabeto(sim)
