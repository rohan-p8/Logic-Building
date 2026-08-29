# Find the factorial of a number using recursion.

def fact(n):

    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

n = int(input("Enter a number: "))

if n < 0:
    print("Factorial does not exist for -ve numbers")
else:
    print(f"The factorial of {n} is: {fact(n)}")


