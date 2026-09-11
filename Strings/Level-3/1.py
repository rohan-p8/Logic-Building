# Reverse a string without using built-in reverse. 

str1 = input("Enter a string to become reveser: ")
rev = ""

for i in range(len(str1) - 1, -1, -1):
	rev = rev + str1[i]

print("\nReversed string: ", rev)


