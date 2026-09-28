# Print pattern -> (A,BC,DEF,GHIJ,JKLMN) using ascii value

n = int(input("Enter number of rows: "))

count = 65 # ascii value of 'A'

for i in range(1, n + 1):

	for j in range(i):
		print(chr(count), end =" ")
		count += 1

	print()

