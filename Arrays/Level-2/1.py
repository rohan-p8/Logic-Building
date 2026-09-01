# Input an element x — check if it exists in the list.

l1 = [14,22,65,79,34,45,89]
print("Given list: ",l1)

n = int(input("Enter element: "))

if n in l1:
	print(f"{n} is present in the list at index {l1.index(n)}")
else:
	print(f"{n} is not present in the list")


