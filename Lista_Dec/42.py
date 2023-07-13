n = int(input())

for y in range(n):
    string_codificada = input()
    string_decodificada = ""

    x = 0
    while x < len(string_codificada):
        caractere = string_codificada[x]
        digito = ""
        x += 1

        while x < len(string_codificada) and string_codificada[x].isdigit():
            digito += string_codificada[x]
            x += 1

        string_decodificada += caractere * int(digito)
    print(string_decodificada)
