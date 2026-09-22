#  Print an Increasing Triangle of Stars 

n = int(input("Enter n to print increasing triangle of stars: "))

for i in range(n):

	for j in range(i + 1):
		print("*", end = " ")
	print()

	