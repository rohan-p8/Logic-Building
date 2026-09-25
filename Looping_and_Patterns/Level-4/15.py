# Print pattern ->(1,23,456,7890,12345)

n = int(input("Enter number of rows: "))
num = 1

for i in range(1, n + 1):

	for j in range(i):
		print(num, end =" ")

		if num >= 9:  # num = (num + 1) % 10
			num = 0
		else:
			num += 1

	print()

