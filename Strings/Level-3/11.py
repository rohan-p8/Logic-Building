#  Reverse string but skip spaces.

str1 = "a b c"
print("Given string: ",str1)

chars = list(str1)

left = 0
right = len(chars) - 1

while left < right:

	if chars[left].isspace():
		left += 1

	elif chars[right].isspace():
		right -= 1

	else:

		chars[left], chars[right] = chars[right], chars[left]

		left += 1
		right -= 1

result = "".join(chars)

print(f"\nReverse string: {result}")

