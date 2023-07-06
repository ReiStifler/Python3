# function
def verifica_fim():
    if A.endswith(B) == True:
        print("ta dentro!!!")
    else:
        print("ta fora...")


# main
A, B = input().split()
verifica_fim()
