palavra = input()
newpalavra = " "

for i in range(len(palavra)):
    if palavra[i] != " ":
        newpalavra += palavra[i] + " "

print(newpalavra.strip())
