# Find the frequency of each character in a string (without using a map). 

str1 = input("Enter string to find freq. of each character: ")

newStr = str1.lower()

freq = {}

for char in newStr:
	if char in freq:
		freq[char] += 1
	else:
		freq[char] = 1

print(f"\n{freq}")


