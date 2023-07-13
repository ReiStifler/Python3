rna_x = input()
rna_y = input()

cout = 0

for x in range(len(rna_x)):
    if rna_y[x] != rna_x[x]:
        cout += 1
print(cout)
