# Find the sum of digits of a number.

n = int(input("Enter a number: "))
sum = 0

while n != 0:
    rem = n % 10
    sum += rem
    n = n // 10

print(f"Sum of digits: {sum}")

