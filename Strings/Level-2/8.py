# Count how many substrings start and end with the same character (simple logic). 

s = "abcab"

length = len(s)

count = 0

for i in range(length):
	
	for j in range(i, length):

		if s[i] == s[j]:
			count += 1

print("Count of substr that start & ends with same char: ",count)

