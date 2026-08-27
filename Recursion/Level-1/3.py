# Print only even numbers from 1 to n recursively.

# need to change in code 

def printEven(n):

    if n <= 0:
        return

    printEven(n - 2)
    print(n)

n = int(input("Enter no.: "))
printEven(n)