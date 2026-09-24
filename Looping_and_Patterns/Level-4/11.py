# Print Stars and Spaces Alternating (Stars and Blank Spaces) 

n = int(input("Enter number of rows: "))

for i in range(1, n + 1):

	for j in range(n - i):
		print("b", end = "")

	for k in range(i):
		print("*", end = "b")

	print()

