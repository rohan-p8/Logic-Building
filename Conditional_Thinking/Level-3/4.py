# Check whether a given integer is single-digit, double-digit, or multi-digit.

n = input("Enter a number: ")

numLen = len(n)

if numLen == 1:
	print("\n This is single digit number")
elif numLen == 2:
	print("\n This is double digit number")

else:
	print("\n This is multi digit number")

	