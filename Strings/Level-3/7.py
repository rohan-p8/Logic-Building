# Print the middle character(s) of a string. 

str1 = input("Enter string to print middle char: ").strip()
length = len(str1)

if length == 0:
	print("Empty string")

else:
	mid = length // 2

	if length % 2 == 0:
		print("\nMiddle character: ",str1[mid - 1 : mid + 1])

	else:
		print("\nMiddle character: ",str1[mid])

