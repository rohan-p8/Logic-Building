# Print cubes of numbers from 1 to n.

n = int(input("Enter number to calculate cubes upto 1 to: "))

for i in range(1, n + 1):
	cube = i * i * i
	print(f"Cube of {i} : {cube}")

	