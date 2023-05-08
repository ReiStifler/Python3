# criando a função denominada 'peso__ideal'

def peso_ideal(a):
    alt = float(a)
    if (alt <= 1.0 and alt >= 2.2):
        return
    # criando os casos para homens e mulheres
    # woman
    peso_mulher = int()
    peso_mulher = ((72.7*(alt))-58)
    # man
    peso_homem = int()
    peso_homem = ((62.1*(alt))-44.7)
    return print('{} {}'.format('%.2f' % peso_mulher, '%.2f' % peso_homem))


# main
a = input()
peso_ideal(a)
