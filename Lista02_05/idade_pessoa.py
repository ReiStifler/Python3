def age(a, b, c):
    dias1, meses1, anos1 = int(a), int(0), int(0)
    dias2, meses2, anos2 = int(b), int(0), int(0)
    dias3, meses3, anos3 = int(c), int(0), int(0)
    if (dias1 and dias2 and dias3 <= 1 and 10**6):
        return
    else:
        if (dias1 >= 360):
            while dias1 >= 360:
                dias1 = dias1 - 360
                anos1 = anos1 + 1
        if (dias1 >= 30):
            while dias1 >= 30:
                dias1 = dias1 - 30
                meses1 = meses1 + 1

        if (dias2 >= 360):
            while dias2 >= 360:
                dias2 = dias2 - 360
                anos2 = anos2 + 1
        if (dias2 >= 30):
            while dias2 >= 30:
                dias2 = dias2 - 30
                meses2 = meses2 + 1

        if (dias3 >= 360):
            while dias3 >= 360:
                dias3 = dias3 - 360
                anos3 = anos3 + 1
        if (dias3 >= 30):
            while dias3 >= 30:
                dias3 = dias3 - 30
                meses3 = meses3 + 1
    return (print('{} {} {}\n{} {} {}\n{} {} {}\n'.format(anos1, meses1, dias1, anos2, meses2, dias2, anos3, meses3, dias3)))


# main
# anos = 360 dias
# meses = 30 dias
pessoa1, pessoa2, pessoa3 = input().split()
age(pessoa1, pessoa2, pessoa3)
