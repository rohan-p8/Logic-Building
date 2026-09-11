# Check if two strings are the reverse of each other. 

str1 = input("Enter string 1: ").lower().strip()

str2 = input("Enter string 2: ").lower().strip()

revEach = True

if len(str1) == len(str2):

	left = 0
	right = len(str2) - 1

	while left < len(str1):

		if str1[left] != str2[right]:
			revEach = False
			break

		left += 1
		right -= 1

	if revEach:
		print(f"\nBoth strings are reverse of each other")
	else:
		print(f"\nBoth are different strings")

else:
	print(f"Both are different strings")

