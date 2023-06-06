def jogadas(a, b):
    if a == b:
        return 0

    if a > b:
        diff = a - b
        if diff % 10 == 0:
            return diff // 10
        else:
            return diff // 10 + 1

    if a < b:
        diff = b - a
        if diff % 10 == 0:
            return diff // 10
        else:
            return diff // 10 + 1


q, w = map(int, (input().split()))
print(jogadas(q, w))
