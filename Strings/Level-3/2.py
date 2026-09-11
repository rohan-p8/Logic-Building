# Reverse each word in a sentence. 

sen = input("Enter string to reverse each word: ")

words = sen.split()

rev = ""

for word in words:

	revWord = ""

	for j in range(len(word) - 1, -1, -1):
		revWord += word[j]

	rev += revWord + " "

print(f"\nString of reversed each word: {rev.strip()}")

