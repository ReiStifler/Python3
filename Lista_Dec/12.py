contador, som_numbers, gt_numbers, numbers = int(), int(), int(), int()

while numbers != -1:
    numbers = int(input())
    if numbers != -1:
        som_numbers += numbers
        gt_numbers += 1
print(int(som_numbers / gt_numbers))
