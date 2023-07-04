figurinhas = int(input())
compradas = int(input())
fileiras = set()

for x in range(compradas):
    figures = int(input())
    fileiras.add(figures)

figurinhas -= len(fileiras)
print(figurinhas)

# while compradas > 0:
#     for x in range(compradas - 1):
#         fileiras += [int(input())]
#     for y in range(compradas - 2):
#         if fileiras[y] != fileiras[y + 1]:
#             figurinhas -= 1
#             print(y)
#     compradas -= 1

# print(figurinhas)
