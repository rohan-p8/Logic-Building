# Check if a number is a perfect number.

n = int(input("Enter a number: "))
sum = 0

for i in range(1, n):
    if n % i == 0:
        sum += i


if sum == n:
    print(f"{n} is Perfect Number")
else:
    print(f"{n} is not Perfect Number")


