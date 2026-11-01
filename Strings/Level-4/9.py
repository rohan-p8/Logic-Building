# Swap case: uppercase → lowercase and lowercase → uppercase. 

str1 = input("Enter string to swap case: ")

new_str = ""

for char in str1:

	if char.islower():
		new_str += char.upper()

	else:
		new_str += char.lower()

print(f"\nAfter swapping the case: {new_str}")