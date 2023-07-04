# QUESTÃO 23
total = int(input())
lista = list(map(int, input().split()))
lista.sort(reverse=True)

soma_time_titular = sum(lista[:11])
soma_banco_reservas = sum(lista[11:22])
diferenca = soma_time_titular - soma_banco_reservas
print(diferenca)
