# Count how many vowels and consonants are in a string. 

str = input("Enter string: ")

vowels = 0
conso = 0

newStr = str.lower()

for char in newStr:
	if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
		vowels += 1
	else:
		conso +=1

print(f"Count of vowels: {vowels}\nCount of consonants: {conso}")

