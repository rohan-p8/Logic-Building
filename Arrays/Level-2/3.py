# Find the first occurrence of a given number. 

list1 = [14,22,79,45,89,14,45,22,79,79]
print("Given list: ", list1)

n = int(input("\nEnter element to find: "))

if n in list1:
	print(f"{n} is found at index {list1.index(n)}")
else:
	print(f"{n} is not present in the list")

