def decompress(x):
    word = ""
    while x > 0:
        letter = chr((x & 31) + 64)
        word += letter
        x = x >> 5
    return word
