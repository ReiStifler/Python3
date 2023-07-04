def soma_aninhada(lista):
    soma = 0

    for elemento in lista:
        if isinstance(elemento, int):
            soma += elemento
        elif isinstance(elemento, list):
            soma += soma_aninhada(elemento)

    return soma
