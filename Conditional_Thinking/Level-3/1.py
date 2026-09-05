# Take a 3-digit number and check if all digits are distinct.

num = input("Enter a 3-digit number: ")

if len(num) == 3 and num.isdigit():
	n1 = num[0]
	n2 = num[1]
	n3 = num[2]

	if n1 != n2 and n1 != n3 and n2 != n3:
		print("\nAll digits are distinct")

	else:
		print("\nDigits are not distinct")

else:
	print("\nPlease enter a valid number")


