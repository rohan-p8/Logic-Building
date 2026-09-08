# Replace every negative number with 0

arr = [22, 14, 8, -13, -27, 88, -45]
print("Given list: ", arr)

newArr = []

for num in arr:
	if num < 0:
		newArr.append(0)

	else:
		newArr.append(num)

print(f"\nNew list: ", newArr)


