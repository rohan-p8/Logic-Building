# Take a character and check if it is a letter, a digit, or neither.

char = input("Enter character to check is it letter or digit: ")

if len(char) == 1:

	if char.isalpha():
		print("\nLetter")

	elif char.isdigit():
		print("\nDigit")

	else:
		print("\nNeither letter or digit")

else:
	print("\nEnter only one character !!!")
