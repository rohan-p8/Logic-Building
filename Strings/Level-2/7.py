# Count how many alphabets are before ‘m’ and after ‘m’ in a given string.

str1 = "computer math"
print("Given string: ",str1)
str1 = str1.replace(" ", "")


countb = 0
counta = 0
foundm = False

for char in str1:
	if char == "m":
		foundm = True
		continue
	if not foundm:
		countb += 1
	else:
		counta += 1

print(f"\nBefore `m` alphabet count: {countb}")
print(f"After `m` alphabet count: {counta}")
