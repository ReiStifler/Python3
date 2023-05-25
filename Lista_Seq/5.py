def dinheiros(litro, vgal1, vgal2):
    redutor = int(litro)
    total_pago = int()
    while redutor > 0:
        if (int(vgal1)) < int(vgal2):
            if redutor >= 1:
                total_pago += int(vgal1)
                redutor -= 1
        elif (int(vgal1)) > int(vgal2):
            if redutor >= 2:
                total_pago += int(vgal2)
                redutor -= 2
            elif redutor == 1:
                total_pago += int(vgal1)
                redutor -= 1
        elif (int(vgal1)) == int(vgal2):
            if redutor >= 1:
                total_pago += int(vgal2)
                redutor -= 2
    return print(total_pago)


# main

lit, gal1, gal2 = input().split()
dinheiros(lit, gal1, gal2)
