def pacotesDeBolacha(m, n, k):
    comer = min(k, m // n)
    funcionarios = m - comer * n
    print(funcionarios)
