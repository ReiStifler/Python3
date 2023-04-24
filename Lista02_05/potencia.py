import math


def powAPC(X, Y):
    X, Y = input().split()
    result = pow(float(X), float(Y))
    print(result)
    return result


# main
powAPC('X'+",", 'Y')
