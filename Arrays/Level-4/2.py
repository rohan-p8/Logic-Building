# Compare two arrays — check if they contain the same elements (ignore order).

lst1 = [15,34,8,22,22]
lst2 = [34,15,8,22]

if sorted(lst1) == sorted(lst2):
	print("\nLists are equal ")
	
else:
	print("\nLists are not equal or contain duplicate elements !!")

