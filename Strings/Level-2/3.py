# Count how many uppercase and lowercase letters a string has. 

str1 = input("Enter string to count upper and lowercase letters: ")

upper = 0
lower = 0

for char in str1:
	if ord(char) >= 65 and ord(char) <= 90:
		upper += 1
	else:
		lower += 1

print(f"\nCount of uppercase letters: {upper}")
print(f"Count of lowercase letters: {lower}")

