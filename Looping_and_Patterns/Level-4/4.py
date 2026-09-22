# Print Square of Stars (n x n Stars) 

n = int(input("Enter n to print square of stars: "))

for i in range(n):

	for j in range(n):
		print("*", end = " ")

	print()