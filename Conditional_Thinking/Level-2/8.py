# Take an alphabet character and check if it lies between ‘a’ and ‘m’ 
# or ‘n’ and ‘z’. 

char = input("Enter one character in lowercase only: ")

if len(char) > 1:
    print("\nEnter only one character !!!")

else:
    newChar = ord(char)

    if newChar >= ord("a") and newChar <= ord("m"):
        print(f"\n{char} is lies between 'a' and 'm'")

    elif newChar >= ord("n") and newChar <= ord("z"):
        print(f"\n{char} is lies between 'n' and 'z'")

        