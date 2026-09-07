# Print the squares of numbers from 1 to n.

n = int(input("Enter number to calculate upto squares 1 to: "))

for i in range(1, n + 1):
	square = i * i
	print(f"Square of {i} : {square}")

