# Reverse the order of words in a sentence. 

str1 = input("Enter sentence to change order of words: ").split()

newStr = ""

for i in range(len(str1) -1, -1, -1):

	newStr += str1[i] + " "

newStr = newStr.strip()
print(f"\nReverse order of words: {newStr}")

