# Roberta
# Montar um lógica melhor


def ritmoMedio(x, y, z, d):
    hora, minuto, segundo, distancia = int(x), int(y), int(z), float(d)

    # condições

    if hora < 0 or hora > 6:
        return
    if minuto < 0 or minuto > 60:
        return
    if segundo < 0 or segundo > 60:
        return
    if distancia < 0 or distancia > 50:
        return

    # recebendo tudo em minutos

    tempo = (hora * 60) + minuto + (segundo / 60)
    ritmo_km = float(tempo) / distancia
    ritmo_int = int(ritmo_km)

    return print("{}".format())


# main
hour, minute, second, distance = input().split()
ritmoMedio(hour, minute, second, distance)
