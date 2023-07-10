def geraEntrada1(mat):
    d = list(mat)
    r = len(list(mat)) - 1
    i = 0
    v = []
    while i <= r:
        v.append(int(f"{d[i]}{d[r-1]}"))
        i += 1
    return v


def geraEntrada2(mat):
    d = []
    for item in mat:
        d.append(int(item))
    return d


def f1(mat):
    d = list(mat)
    i = len(d)
    _str = ""
    while i > 1:
        _str += f"{(d[i-1])}-"
        i -= 1
    return _str


def f2(mat):
    d = geraEntrada2(mat)
    _str = ""
    for item in d:
        if item % 2 == 0:
            _str = _str + f"{item}"
    return _str


def f3(mat):
    d = geraEntrada2(mat)
    acumula = 20
    for i in range(len(d)):
        acumula += d[i]
        if d[i] > 0 and not d[i] % 3:
            break
    return acumula


def f4(mat):
    acumula = 1
    d = geraEntrada2(mat)
    dim = len(d)
    for item in d:
        if item % 2 == 0:
            index1 = 0
            index2 = dim / 2
        else:
            index1 = dim // 2
            index2 = dim - 1
        while index1 < index2:
            itemAux = d[index1]
            if itemAux > 0:
                acumula += d[index1]
            index1 += 1
    return acumula


matricula = input()
print(geraEntrada1(matricula))
print(geraEntrada2(matricula))
print(f1(matricula))
print(f2(matricula))
print(f3(matricula))
print(f4(matricula))
