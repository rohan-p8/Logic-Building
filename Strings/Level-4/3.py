# Replace all vowels with ‘*’.

str1 = input("Enter string to replace all vowels with '*': ")

new_str = ""
vowels = "aeiouAEIOU"

for char in str1:

	if char not in vowels:
		new_str += char

	else:
		new_str += '*'

print(f"\nAfter replacing: {new_str}")

