senha = input()

if len(senha) < 6 or len(senha) > 32:
    print("Senha invalida.")
elif not senha.isalnum():
    print("Senha invalida.")
else:
    maiuscula = False
    minuscula = False
    num = False

    for caractere in senha:
        if caractere.isupper():
            maiuscula = True
        elif caractere.islower():
            minuscula = True
        elif caractere.isdigit():
            num = True

    if maiuscula and minuscula and num:
        print("Senha valida.")
    else:
        print("Senha invalida.")
