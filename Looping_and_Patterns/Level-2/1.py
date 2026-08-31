# Count the number of digits in a given number.

n = int(input("Enter a number: "))
digit = 0

while n != 0:
    rem = n % 10
    digit += 1
    n = n // 10

print(f"There are {digit} digits in given number")

