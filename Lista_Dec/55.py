s = input()

frase = ""

for letra in range(len(s)):
    if (
        letra < len(s)
        and s[letra] == "n"
        and (s[letra + 1] == "b" or s[letra + 1] == "p")
    ):
        frase += "m"
    else:
        frase += s[letra]

print(frase)
