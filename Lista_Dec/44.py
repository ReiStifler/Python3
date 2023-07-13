q = int(input())

for x in range(q):
    l, r, s = input().split()
    l = int(l)
    r = int(r)
    print(s[l : r + 1])
