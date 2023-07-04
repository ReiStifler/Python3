elementos = input().strip().split()

if len(set(elementos)) < len(elementos):
    print(True)
else:
    print(False)
