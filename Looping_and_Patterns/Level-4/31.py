# Print centered pattern -> (5,545,54345)

n = int(input("Enter number of rows: "))

count = 5

for i in range(1, n + 1):

	for s in range(n - i):
		print(" ", end = "")

	for j in range(n, n - i, -1):
		print(j, end = "")

	for k in range(n - i + 2, n + 1):
		print(k, end = "")

	print()

