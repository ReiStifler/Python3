# Dada a descrição de um horário, diga quantos segundos já se passaram no dia conforme o formato definido abaixo.

# Entrada
# A entrada consiste de uma linha, composta por três números inteiros representando um horário no dia, apresentados no formato "hh:mm:ss" (hora:minutos:segundo).

# Saída
# A saída deve ser composta de uma linha apresentando a mensagem: "La se foram X segundos que nao voltam mais...", onde X
#  é a quantidade total de segundos decorridos desde o início do horário.

# For example:

# Input	Result
# 00:00:01
# La se foram 1 segundos que nao voltam mais...
# 00:01:01
# La se foram 61 segundos que nao voltam mais...
# 01:01:01
# La se foram 3661 segundos que nao voltam mais...

def converction(a, b, c):
    horas, minutos, segundos = int(a), int(b), int(c)
    if (horas >= 1):
        while horas >= 1:
            horas = horas - 1
            segundos = segundos + 3600
    if (minutos >= 1):
        while minutos >= 1:
            minutos = minutos - 1
            segundos = segundos + 60
    print('La se foram {} segundos que nao voltam mais...'.format(segundos))


# main
a, b, c = input().split(':')
converction(a, b, c)
