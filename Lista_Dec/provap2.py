def geraValor1(entrada):
    return entrada % 100000 // 1000


def geraValor2(entrada):
    return entrada % 1000 // 10


def geraValor4(entrada):
    return entrada % 10000 // 100


def geraValor5(entrada):
    return entrada % 10000 // 10


matricula = int(input())
a = geraValor2(matricula)
print(a)
b = geraValor4(matricula) * 0.1
print(b)
c = geraValor5(matricula)
print(c)
print(f"{ a + 7* b /3 -( c /2):.1f}")
delta = (a + 7 * b) / (3 - (c / 2))
print("%.1f" % delta)
