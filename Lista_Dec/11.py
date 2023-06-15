qtd_numbers = int(input())
list_numbers = []

for x in range(qtd_numbers):
    numbers = int(input())
    list_numbers.append(numbers)

print(("Menor: {}".format(min(list_numbers))))
print(("Maior: {}".format(max(list_numbers))))
