# Count how many times a given element appears.

list1 = [14,22,79,45,89,14,45,22,79,79]
print("Given list: ", list1)

n = int(input("\nEnter element to find: "))
count = 0

for item in list1:
	if item == n:
		count += 1
	else:
		count == 0

print(f"{n} appears {count} times in the list")


