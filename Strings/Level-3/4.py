# Check whether a string is a palindrome.

str1 = input("Enter string to check palindrome or not: ").lower().replace(" ", "")

rev = ""

for i in range(len(str1)-1, -1, -1):

	rev += str1[i]


if str1 == rev:
	print(f"\nThe given string - {str1}, is Palindrome")
	
else:
	print(f"\nThe given string - {str1}, is NOT Palindrome")

