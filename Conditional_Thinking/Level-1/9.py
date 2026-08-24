# Take a character and check if it’s a vowel or consonant.

char = input("Enter a character : ")

if len(char) != 1:
    print("Enter exactly on character")

else:

    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        print(f"{char} is vowel")
    else:
        print(f"{char} is consonant")
