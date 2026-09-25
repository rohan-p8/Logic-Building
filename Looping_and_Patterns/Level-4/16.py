# Print pattern ->(1,01,010,1010,10101)

n = int(input("Enter number of rows: "))

num = 1

for i in range(1, n + 1):

	for j in range(i):
		print(num, end =" ")
		num = 1 - num

		# 2nd logic
		# if num == 1:
		# 	num = 0
		# else:
		# 	num = 1
		
	print()

