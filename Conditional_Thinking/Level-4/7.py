# Take a single digit (0–9) and print its word form (“Zero” to “Nine”). 

digit = input("Enter digit (0-9): ")

num = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]

if len(digit) == 1 and digit.isdigit():

	print(f"\nDigit to word: {num[int(digit)]}")

else:
	print("\nEnter only single digit from (0-9)!!")

