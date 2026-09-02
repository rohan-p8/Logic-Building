# Find the sum of even elements only.

list1 = [14,22,79,45,89,14,45,22,79,79]

sum1 = 0

for num in list1:
	if num % 2 == 0:
		sum1 += num

print(f"Sum of even element is {sum1}")

