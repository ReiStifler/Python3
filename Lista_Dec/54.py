palavra = input()

vogais = ["A", "O", "Y", "E", "U", "I"]
palavra_nova = ""

for letras in palavra:
    if letras.upper() not in vogais:
        palavra_nova += "." + letras.lower()
print(palavra_nova)
