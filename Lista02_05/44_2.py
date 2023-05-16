def ritmoMedio(h, m, s, d):
    totalminutos = h * 60 + m + s / 60
    media = float(totalminutos) / float(d)
    minutos = int(media)
    restante = media - float(minutos)
    segundos = int(restante * 60)
    print("{:02d}".format(minutos) + ":" + "{:02d}".format(segundos) + " min/km")
