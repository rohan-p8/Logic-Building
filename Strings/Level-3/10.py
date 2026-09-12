# Reverse only characters, keeping digits in place. 

str1 = input("Enter string to reverse only characters not digits: ").strip()

chars = list(str1)

left = 0
right = len(chars) - 1

while left < right:

	if not chars[left].isalpha():
		left += 1

	elif not chars[right].isalpha():
		right -= 1

	else:

		chars[left], chars[right] = chars[right], chars[left]

		left += 1
		right -= 1

result = "".join(chars)

print(f"\nReverse only characters: {result}")

