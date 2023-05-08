def binario(a):
    entrada = int(a)
    binary = ''

# metódo da divisão sucessiva utlizando o resto e a resultante da divisão

    if (entrada == 0):
        return print('0b0')
    else:
        while entrada > 0:
            # obtem os valores do resto da divisão e armazena em uma string
            resto = entrada % 2
            # com a entrada sendo um numero inteiro, recebe o resultado da divisão em forma de divisão exata
            entrada = entrada // 2
            # salva todos os valores do resto em forma de string e adiciona eles junto ao valor do resultado da divisão exata
            binary = str(resto) + binary
    return print('0b{}'.format(binary))


# main
for i in range(5):
    a = input()
    binario(a)
