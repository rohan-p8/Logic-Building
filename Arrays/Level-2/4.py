# Find the last occurrence of a given number

list1 = [14,22,79,45,89,14,45,22,79,79]
print("Given list: ", list1)

n = int(input("\nEnter element to find: "))

ind = -1

for i in range(len(list1)):
	if list1[i] == n:
		ind = i
print(f"Last occurrence of {n} at index {ind}")


# using list slicing

# ind = len(list1) - 1 - list1[::-1].index(n)

# print(f"Last occurrence of {n} is at index {ind}")

