# para cada parte do tabuleiro, tens se N X M, que representam a quantidade de casas presentes, cada peça de domino ocupa 2 casas
def dominos(n, m):
    return print((int(n) * int(m)) // 2)


# main
t, x = input().split()
dominos(t, x)
