# Count how many times a given character appears in a string. 

str1 = "This is first string that i write and i am also fine"
newStr = str1.lower()
print(newStr)

count = 0

char = input("\nEnter single character: ")

for item in newStr:
	if item == char:
		count += 1

print(count)

