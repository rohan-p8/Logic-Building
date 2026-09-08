# Replace all even numbers with 1 and all odd with 0.

list1 = [13,15,8,27,89,46,18,3,9,88]
print("Given list: ", list1)

newList = []

for i in range(len(list1)):
	if list1[i] % 2 == 0:
		list1[i] = 1
	else:
		list1[i] = 0

print("\nReplaced List: ", list1)

