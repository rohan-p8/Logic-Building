#  Count how many elements are perfect squares.

# Perfect squares means : ex. num = 49 
# if sqrt of 49 = x then x * x = num

import math

list1 = [25,30,9,49,57,86,81,36]

print("Given list: ", list1)
count = 0

for num in list1:
	if num >= 0:
		root = math.isqrt(num)

		if root * root == num:
			count += 1

print(f"Count of Perfect squares: {count}")

