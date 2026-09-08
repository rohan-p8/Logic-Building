# Create a new array containing only even elements.

arr = [12,2,24,43,56,88,99,64,13,8]
print("Given list: ", arr)

newArr = []

for num in arr:
	if num % 2 == 0:
		newArr.append(num)

print(f"\nList of even elements: \n", newArr)

