# Print all prime numbers between 1 and N. 

n = int(input("Enter number: "))
print(f"\nPrime numbers between 1 and {n} are: ")

for num in range(2, n + 1):
	if num > 1:
		for i in range(2, num):
			if num % i == 0:
				break
		else:
			print(num, end=" ")

