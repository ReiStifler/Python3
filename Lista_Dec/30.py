def chinelo(chbill, cht):
    for i, tamanho in enumerate(cht):
        if tamanho >= chbill:
            return i
    return -1


chbill = int(input())
cht = list(map(int, input().split()))
cht.sort()
posicao = chinelo(chbill, cht)
print(posicao)
