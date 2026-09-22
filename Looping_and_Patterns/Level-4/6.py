# Print a Right-Aligned Triangle of Stars 

n = int(input("Enter n for printing Right-Aligned Triangle of Stars: "))

for i in range(1, n + 1):

	for j in range(n - i):

		print(" ", end = " ")

	for k in range(i):
		print("*", end = " ")


	print()

