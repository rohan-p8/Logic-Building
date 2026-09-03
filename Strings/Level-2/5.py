# Count how many spaces are there in a sentence. 

sentence = input("Enter sentence: ")

sentence = sentence.strip()

count = 0

for i in range(len(sentence)):
	if sentence[i] == " ":
		count += 1
	
print(f"Count of spaces: {count}")

