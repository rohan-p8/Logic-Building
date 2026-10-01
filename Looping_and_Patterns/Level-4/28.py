# Print pattern -> (*,**,***,***,**,*)

n = int(input("Enter number of rows: "))

for i in range(1, n + 1):

	for j in range(i):
		print("*", end = "")

	print()

for k in range(n, 0, -1):

	for j in range(k):
		print("*", end = "")

	print()

	