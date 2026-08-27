#  Print numbers from 1 to n using recursion.

def printNo(no):

    if no <= 0:
        return

    
    printNo(no - 1)
    print(no)

no = int(input("Enter no.: "))
printNo(no)

