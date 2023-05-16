def age(a):
    dias1 = int(a)
    anos1 = input()
    meses1 = input()

    if dias1 >= 360:
        while dias1 >= 360:
            dias1 = dias1 - 360
            anos1 = anos1 + 1
    if dias1 >= 30:
        while dias1 >= 30:
            dias1 = dias1 - 30
            meses1 = meses1 + 1

    print(f"{anos1} ano(s), {meses1} mes(es) e {dias1} dia(s)")


# main
a, b, c = input().split()
age(a)
age(b)
age(c)
