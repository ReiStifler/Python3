# O jovem Guilson é o responsável por receber as compras de supermercado para seus pais em tempos de pandemia. Ultimamente,
# Guilson esta bastante estressado por ter que cuidar de toda a higienização dos produtos antes de guardá-los nos devidos lugares.
# Construa um programa que estima o tempo que Guilson irá levar para higienizar uma determinada compra de supermercado sabendo que ele leva entre 1 e 3
# minutos por produto para retirá-lo da sacola, lavá-lo, secá-lo e guardá-lo.

# Entrada
# A entrada consiste em um número inteiro indicando a quantidade de produtos (0<produtos
# ) da lista de compras.

# Saída
# Apresente, em uma linha, a quantidade de segundos gastos no melhor e pior casos, conforme os exemplos.

# For example:

# Input	Result
# 10
# Entre 600 e 1800.
# 15
# Entre 900 e 2700.

# main

qtd_itens = int(input())
min = 60

melhor_caso = (qtd_itens * 1) * min
pior_caso = (qtd_itens * 3) * min

print("Entre {} e {}.".format(melhor_caso, pior_caso))
