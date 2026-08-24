# Take three numbers and print the largest.

n1, n2, n3 = map(int, input("Enter three no.: ").split())

if n1 > n2 and n1 > n3:
    print(f"{n1} is largest number")
elif n2 > n1 and n2 > n3:
    print(f"{n2} is largest number")
else:
    print(f"{n3} is largest number")

    