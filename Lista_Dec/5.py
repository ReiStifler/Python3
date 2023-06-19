number = int(input())

if number >= 0:
    print(str(number)[::-1])
else:
    print("-" + str(number)[:0:-1])
