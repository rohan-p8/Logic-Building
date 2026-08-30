# Check if one of two given numbers is a multiple of the other.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a == 0 or b == 0:
    print("Zero is multiple of any integer, but you cannot divide by zero")
    
else:
    if a % b == 0 or b % a == 0:
        print(f"{a} is multiple of {b}")

    else:
        print("Both numbers are not multiple of each other")

