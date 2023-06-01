def pitorestico(a, b, c):
    if int(a) % 2 == 0 and int(a) % 3 == 0 and int(a) % 5 == 0:
        if int(b) % 2 == 0 and int(b) % 3 == 0 and int(b) % 5 == 0:
            if int(c) % 2 == 0 and int(c) % 3 == 0 and int(c) % 5 == 0:
                return print("Pitorestico!!!")
            else:
                return print("Nao foi dessa vez")
        else:
            return print("Nao foi dessa vez")
    else:
        return print("Nao foi dessa vez")


# main

q, w, e = input().split()
pitorestico(q, w, e)
