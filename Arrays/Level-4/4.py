# Find the common elements between two lists.

lst1 = [1,34,8,22,88,63]
lst2 = [15,3,8,22,18]

commonElements = []

for element in lst1:
	if element in lst2 and element not in commonElements:
		commonElements.append(element)

print(commonElements)
