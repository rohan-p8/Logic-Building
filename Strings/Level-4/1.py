# Remove all vowels from a string.

str1 = input("Enter string to remove vowels from it: ")

newStr = ""
vowels = "aeiouAEIOU"

for char in str1:

	if char not in vowels:
		newStr += char

print(f"\nAfter removing vowels: {newStr}")
