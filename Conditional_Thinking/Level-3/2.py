# Take a 3-digit number and determine if the middle digit is the largest, smallest, or 
# neither. 

num = input("Enter a 3 digit number: ")

if len(num) == 3 and num.isdigit():
	n1 = int(num[0])
	n2 = int(num[1])
	n3 = int(num[2])

	if n2 > n1 and n2 > n3:
		print("\nMiddle number is largest than others")

	elif n2 < n1 and n2 < n3:
		print("\nMiddle number is smaller number than others")

	else:
		print("\nMiddle number is Neither large nor small")

else:
	print("\nEnter a valid 3 digit number")

