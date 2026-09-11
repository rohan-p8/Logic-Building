# Reverse the order of words in a sentence. 

str1 = input("Enter sentence to change order of words: ").split()
# str1 = "Hello rohan".split()

newStr = ""
revOrder = ""

for i in range(len(str1) -1, -1, -1):

	newStr += str1[i] + " "

print(f"\nReverse order of words: {newStr}")

