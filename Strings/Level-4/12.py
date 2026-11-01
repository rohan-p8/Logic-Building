# Shift each character by 1 (e.g., “abc” → “bcd”).

str1 = input("Enter string: ")

new_str = ""


for char in str1:

	if 'a' <= char <= 'z':
		new_str += chr((ord(char) - ord('a') + 1) % 26 + ord('a'))

	elif 'A' <= char <= 'Z':
		new_str += chr((ord(char) - ord('A') + 1) % 26 + ord('A'))

	else:
		new_str += char

print(f"\nAfter shifting char by 1: {new_str}")