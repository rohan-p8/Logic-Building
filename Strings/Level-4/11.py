# Shift each character by 1 (e.g., “abc” → “bcd”).

str1 = input("Enter string: ")
new_str = ""

for char in str1:

	new_str += chr(ord(char) + 1)

print(f"\nAfter shifting char by 1: {new_str}")
