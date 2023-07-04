N = int(input())
tempos = list(map(int, input().strip().split()))
tmin = min(tempos)
diferencas = [tempo - tmin for tempo in tempos]
print(" ".join(map(str, diferencas)))
