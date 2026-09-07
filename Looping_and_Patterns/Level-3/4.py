# Find HCF (GCD) of two numbers using loops.

n1, n2 = map(int, input("Enter two numbers to calculate HCF (GCD): ").split())
minNum = min(n1, n2)

for i in range(minNum, 0, -1):
	if n1 % i == 0 and n2 % i == 0:
		print(f"\nHCF of {n1} and {n2} is {i}")
		break

	