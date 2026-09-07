# Find the sum of all factors of a number.

n = int(input("Enter number to find sum of factors: "))
sum1 = 0

for i in range(1, n + 1):
	if n % i == 0:
		print(i)
		sum1 = sum1 + i

print(f"\nSum of factors: {sum1}")

