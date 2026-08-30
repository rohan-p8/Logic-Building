# Take two numbers and determine whether both are even, both are odd, or one is 
# even and one is odd

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a % 2 == 0 and b % 2 == 0:
    print(f"Both {a} and {b} are even numbers")

elif a % 2 == 1 and b % 2 == 1:
    print(f"Both {a} and {b} are odd numbers")

elif a % 2 == 0 and b % 2 == 1:
    print(f"{a} is even number and {b} is odd number")

elif a % 2 == 1 and b % 2 == 0:
    print(f"{a} is odd number and {b} is even number")

