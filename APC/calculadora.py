'teste de uma calculadora simples utilizando for e while para cada uma das operações'
soma = 0
no_condicion = 0
print('para finalizar o código, digite : 5')

while no_condicion < 1:
    print("\nescolha a operacao\n"
          ' 1 = soma\n'
          ' 2 = multiplicação\n'
          ' 3 = subtração\n'
          ' 4 = divisão\n')
    escolha = int(input())

    if escolha == 1:
        print("Quantos Numeros?", '\n')
        tamanho = int(input())
        print("Digite os valores a serem somados\n")

        for i in range(tamanho):
            numbers = int(input())
            soma = soma + numbers
        print('\nResultado :', soma)

    if escolha == 2:
        print("Quantos Numeros?", '\n')
        tamanho = int(input())
        print("Digite os valores a serem multiplicados\n")

        for i in range(tamanho):
            numbers = int(input())
            soma = soma * numbers
        print('\nResultado :', soma)

    if escolha == 3:
        print("Quantos Numeros?", '\n')
        tamanho = int(input())
        print("Digite os valores a serem subtraidos\n")

        for i in range(tamanho):
            numbers = int(input())
            soma = soma - numbers
        print('\nResultado :', soma)

    if escolha == 4:
        print("Quantos Numeros?", '\n')
        tamanho = int(input())
        print("Digite os valores a serem divididos\n")

        for i in range(tamanho):
            numbers = int(input())
            soma = soma / numbers
        print('\nResultado :', soma)

    if escolha == 5:
        break
