# Print the string after removing all digits.

str1 = input("Enter string to remove all digits: ")

new_str = ""

for char in str1:

	if not char.isdigit():
		new_str += char

print(f"\nAfter removing digits: {new_str}")

