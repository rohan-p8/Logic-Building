# Print pattern -> (*,**,***,****,***,**,*)

n = int(input("Enter number of rows: "))

for i in range(1, n + 1):

	for j in range(i):
		print("*", end = "")

	print()

for k in range(n, 1, -1):

	for j in range(1, k):
		print("*", end = "")
	
	print()

