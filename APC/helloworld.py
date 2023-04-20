print("Qual o tamanho do vosso for?", '\n')
tamanho = int(input())
soma = 0

for i in range(tamanho):
    numbers = int(input())
    soma = soma + numbers

print('\n', 'Vossa soma deu o valor =', soma)
