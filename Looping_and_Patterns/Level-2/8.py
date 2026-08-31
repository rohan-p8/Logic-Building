# Check if a number is prime or not. 

n = int(input("Enter a number: "))

if n > 1:

    for i in range(2, n):
        if n % i == 0:
            print("Not a Prime number")
            break

    else:
        print("Prime number")
else:
    print("Not a prime number")

