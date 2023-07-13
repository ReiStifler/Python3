s = input()

if s == s[::-1]:
    if len(s) % 2 == 0:
        print("OFF")
    else:
        print("ON")

else:
    cout = 0
    for x in range(len(s) // 2):
        if s[x] != s[-x - 1]:
            cout += 1
    if cout == 1:
        print("ON")
    else:
        print("OFF")
