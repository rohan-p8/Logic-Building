# Remove duplicate characters from a string.

str1 = input("Enter string to remove duplicate char: ")

newStr = ""

for char in str1:
	if char not in newStr:
		newStr += char

print(f"Updated string: {newStr}")

