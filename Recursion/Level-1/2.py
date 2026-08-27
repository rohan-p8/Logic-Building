# Print numbers from n down to 1 using recursion. 

def printNo(n):

    if n <= 0:
        return

    print(n)
    printNo(n - 1)

n = int(input("Enter no.: "))
printNo(n)

