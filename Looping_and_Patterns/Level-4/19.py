# Print pattern -> (A,BB,CCC,DDDD)

n = int(input("Enter number of rows: "))

count = 65

for i in range(1, n + 1):

	for j in range(i):
		print(chr(count), end =" ")
		
	count += 1

	print()

