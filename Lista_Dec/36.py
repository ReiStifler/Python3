def remove_caractere(s):
    n = len(s)

    for i in range(n - 1):
        if s[i] > s[i + 1]:
            return s[:i] + s[i + 1 :]

    return s[:-1]


n = int(input())
s = input()
nova_string = remove_caractere(s)
print(nova_string)
