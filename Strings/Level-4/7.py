# Keep only the first occurrence of each character (same as remove duplicate chars)

str1 = input("Enter string to keep first occurrence: ")

unique = set()

new_str = ""

for char in str1:

	if char not in unique:
		unique.add(char)
		new_str += char

print(f"\nKeeping only first occurrence: {new_str}")

