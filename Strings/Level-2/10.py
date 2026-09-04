#  Count how many words end with ‘s’

sen = "This is the pes football games"
sen = sen.lower().split()
count = 0

print(sen)

for word in sen:
	if word[-1] == 's':
		count += 1

print("\nCount of words with end 's': ",count)

