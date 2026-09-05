# Check if a number is a multiple of 7 or ends with 7.

num =abs(int(input("Enter a number: ")))

if num % 7 == 0 or num % 10 == 7:
	print(f"\n{num} is multiple of 7 or ends with 7")

else:
	print(f"\n{num} is not multiple nor ends with 7")

	