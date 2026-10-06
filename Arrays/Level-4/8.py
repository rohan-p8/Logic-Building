# Find element-wise product of two lists. 

lst1 = [1,34,88,63]
lst2 = [15,3,8,18]

newLst = []

if len(lst1) != len(lst2):
	print("Lists are not equal (lengths differ)!")

else:
	for i in range(len(lst1)):
		prod = lst1[i] * lst2[i]

		newLst.append(prod)

print(f"\nElement wise product of two lists: {newLst}")
