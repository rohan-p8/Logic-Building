 # Print the product of digits of a given number. 

n = int(input("Enter a number: "))
prod = 1

while n != 0:
    rem = n % 10
    prod = prod * rem
    n = n // 10

print(f"Product of digits of given number is : ", prod)