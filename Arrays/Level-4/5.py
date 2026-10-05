# Find elements that are in one list but not in the other.

lst1 = [1,34,8,22,88,63]
lst2 = [15,3,8,22,18]

uniqueElements = []

#Elements in lst1 but not in lst2
for x in lst1:
	if x not in lst2 and x not in uniqueElements:
		uniqueElements.append(x)

for y in lst2:	
	if y not in lst1 and y not in uniqueElements:
		uniqueElements.append(y)

print(uniqueElements)
