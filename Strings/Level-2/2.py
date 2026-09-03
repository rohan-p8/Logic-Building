# Count the number of digits, letters, and special characters in a string. 

str1 = input("Enter string to count letters, digits and special characters: ")
newStr = str1.lower()

digits = 0
letters = 0
sChar = 0

for char in newStr:
	if ord(char) >= 97 and ord(char) <= 122:
		letters += 1
	elif ord(char) >= 48 and ord(char) <= 57:
		digits += 1
	else:
		sChar += 1

print(f"\nCount of letters: {letters}\nCount of digits: {digits}\nCount of special characters: {sChar}")

