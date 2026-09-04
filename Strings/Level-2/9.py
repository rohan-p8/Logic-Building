# Print how many words start with a vowel in a sentence.

sen = "Hello rohan how are u e i o ouch"
sen = sen.lower()
print(sen)

words = sen.split()
count = 0
vowels = ['a','e','i','o','u']

for word in words:
	if word[0] in vowels:
		count += 1

print("\nCount of words start with vowels: ",count)

