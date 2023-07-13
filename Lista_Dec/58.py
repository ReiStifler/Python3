string = input()

vowels = ["a", "e", "i", "o", "u"]

for vowel in vowels:
    new_string = ""
    for letter in string:
        if letter.islower() and letter in vowels:
            new_string += vowel
        else:
            new_string += letter
    print(new_string)
