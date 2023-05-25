def banner(a):
    if int(a) > 0 and int(a) % 2 == 0:
        print("| | | | | | | | | |")
    elif int(a) > 0 and int(a) % 2 != 0:
        print("- - - - - - - - - -")
    elif int(a) < 0 and int(a) % 2 == 0:
        print(". . . . . . . . . .")
    elif int(a) < 0 and int(a) % 2 != 0:
        print("= = = = = = = = = =")


# main

val = input()
banner(val)
