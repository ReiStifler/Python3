def Ordena(a, b, c):
    numbers = [int(a), int(b), int(c)]
    numbers.sort(reverse=False)
    return print("(" + ", ".join(str(num) for num in numbers) + ")")


# main

e, r, t = input().split()
Ordena(e, r, t)
