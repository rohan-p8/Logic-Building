#  Print an Increasing Triangle of Stars 

n = int(input("Enter n to print increasing triangle of stars: "))

for i in range(1, n + 1):

	for j in range(i):
		print("*", end = " ")
	print()

