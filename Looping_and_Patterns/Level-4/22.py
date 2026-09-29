# Centered triangle pattern: (A,BC,DEF,GHIJ) back to 'A'

n = int(input("Enter number of rows: "))

char = 0

for i in range(1, n + 1):

	for j in range(n - i):
		print(" ", end = "")
	
	for k in range(i):
		print(chr(65 + (char % 26)), end= " ")
		char += 1

	print()