def converte(Fahrenheit):
    Fahrenheit = float(input())
    Celsius = ((5/9)*((Fahrenheit - 32)))
    print("%0.1f" % Celsius)
    return Celsius


converte('Celsius')
