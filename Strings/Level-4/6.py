# Remove duplicate characters from a string.

str1 = input("Enter string to remove duplicate characters: ")

seen = set()
result = ""

for char in str1:

	if char not in seen:
		seen.add(char)
		result += char

print(f"\nAfter removing duplicates: {result}")

