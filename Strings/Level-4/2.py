# Remove all spaces from a string.

str1 = input("Enter sentence to remove whitespaces: ")

newStr = ""

for char in str1:

	if char != " ":
		newStr += char

print(f"\nAfter removing spaces: {newStr}")


# Using replace():

# str1 = input("Enter sentence: ")
# new_str = str1.replace(" ", "")
# print(f"\nAfter removing spaces: {new_str}")
