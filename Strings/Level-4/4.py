# Replace all spaces with ‘_’. 

str1 = input("Enter string to replace whitespaces with '_': ")

new_str = ""

for char in str1:

	if char != " ":
		new_str += char

	else:
		new_str += '_'

print(new_str)

