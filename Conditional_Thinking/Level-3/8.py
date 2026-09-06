# Check if a number lies within the range [100, 999]. 

num = int(input("Enter a number: "))

if num > 0:

	if num >= 100 and num < 1000:
		print(f"\n{num} lies between 100 and 999")

	else:
		print(f"\n{num} is not between 100 and 999")

else:
	print("\nEnter valid number !!!")

