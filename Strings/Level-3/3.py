# Reverse the order of words in a sentence. 

str1 = input("Enter sentence to change order of words: ")
newStr = str1.split()

order = ""

for word in newStr:

	rev = ""

	for i in range(len(word) - 1, -1, -1):

		rev += word[i]

	order += rev + " "

print(f"\nReverse order of words: {order}")

