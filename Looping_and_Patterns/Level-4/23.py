# Centered pattern of Odd no. of alphabets: (A,BCD,EFGHI)

n = int(input("Enter number of rows: "))

char = 0

for i in range(1, n + 1):

	for j in range(n - i):
		print(" ", end = " ")
	
	for k in range(2 * i - 1):
		print(chr(65 + (char % 26)), end= " ")
		char += 1

	print()
	