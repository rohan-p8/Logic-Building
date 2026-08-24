#  Take a character and check whether it’s uppercase, lowercase, 
# a digit, or a special character. 

char = input("Enter a character : ")

if len(char) != 1:
    print("Enter exactly one character")
else:

    if char.isupper():
        print(f"{char} is letter in Uppercase" )
    elif char.islower():
        print(f"{char} is letter in Lowercase")
    elif char.isdigit():
        print(f"{char} is a digit")
    else:
        print(f"{char} is special character")

