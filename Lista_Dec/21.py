N = int(input())
tempos = list(map(int, input().strip().split()))

tmax = max(tempos)

diferencas = [tmax - tempo for tempo in tempos]

print(" ".join(map(str, diferencas)))
