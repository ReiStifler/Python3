def converte(Fahrenheit):
    Fahrenheit = float(input())
    Celsius = ((5/9)*((Fahrenheit - 32)))
    return (print("%.1f" % Celsius))


converte('Celsius')
