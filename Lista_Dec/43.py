def reverte_string(l, r, s):
    substr = s[l : r + 1]
    reverso = substr[::-1]
    return reverso


q = int(input())

for x in range(q):
    l, r, s = input().split()
    l = int(l)
    r = int(r)

    print(reverte_string(l, r, s))
