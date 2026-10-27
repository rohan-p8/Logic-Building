# Remove consecutive duplicate characters (e.g., “aaabb” → “ab”).

str1 = input("Enter string: ")

if not str1:
	new_str = ""

else:
	new_str = str1[0]

	for i in range(1, len(str1)):
		if str1[i] != str1[i - 1]:
			new_str += str1[i]

print(f"\nAfter removing consecutive duplicates: {new_str}")