# Print a Centered Pyramid of Stars 

n = int(input("Enter n print centered pyramid of stars: "))

for i in range(1, n + 1):

	for j in range(n - i):
		print(" ", end = "")

	for k in range(i):
		print("*", end = " ")

	print()