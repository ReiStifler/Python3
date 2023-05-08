def maiorAB(a, b):
    if (int(a) > int(b)):
        maior = a
        return (print(maior))
    else:
        maior = b
        return (print(maior))


for math in range(5):
    a, b = input().split()
    maiorAB(a, b)
