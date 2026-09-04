#  Check if a number is perfect (sum of factors equals number).

n = int(input("Enter no. to check it is perfect or not: "))

sum1 = 0

for i in range(1, n):
	if n % i == 0:
		sum1 += 1

if sum1 == n:
	print(f"\n{n} is Perfect number")
else:
	print(f"\n{n} is not perfect number")

