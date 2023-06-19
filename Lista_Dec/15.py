number = int(input())
somador = int()

while number > 0:
    numbers1, numbers2, number3 = map(int, (input().split()))
    somador += numbers1 + numbers2 + number3
    number -= 1
if somador == 0:
    print("ESTACIONARIO")
else:
    print("MOVIMENTO")
