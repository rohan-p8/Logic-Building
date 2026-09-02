# Find the sum of odd elements only. 

list1 = [14,22,79,45,89,14,45,22,79,79]

odd = 0

for num in list1:
	if num % 2 == 1:
		odd += num

print(f"Sum of odd elements is {odd}")

