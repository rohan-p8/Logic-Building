# Take a 4-digit number and check if the first and last digits are equal.

num = input("Enter 4-digit number: ")

if len(num) == 4 and num.isdigit():

	n1 = int(num[0])
	n2 = int(num[3])

	if n1 == n2:
		print("\nFirst & Last digits are equal")

	else:
		print("\nFirst & Last digits are not equal")
else:
	print("\nEnter valid 4-digit number")

