# Print centered triangle pattern of alphabets: (A,BC,DEF,GHIJ)

n = int(input("Enter number of rows: "))

char = 65

for i in range(1, n + 1):

	for j in range(n - i):
		print(" ", end = "")
	
	for k in range(i):
		print(chr(char), end= " ")
		char += 1

	print()
	 
