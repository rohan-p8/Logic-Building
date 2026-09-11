# Remove the first and last character and print the remaining string.

str1 = input("Enter string to remove first & last character:").strip()
newStr = ""
if len(str1) <= 2:
	print("String contains only 0, 1 or 2 characters !!!")

else:
	for i in range(1, len(str1) - 1):
		newStr += str1[i]
	
	print(f"After removing: {newStr}")

