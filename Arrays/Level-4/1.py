# Compare two lists — check if they are equal (same elements & order).

lst1 = [15,34,8,22]
lst2 = [15,3,8,22]

if len(lst1) != len(lst2):
	print("Lists are not equal (lengths differ)!")

else:
	for i in range(len(lst1)):
		if lst1[i] != lst2[i]:
			print(f"Mismatch found at index {i}: {lst1[i]} != {lst2[i]}")
			print("Lists are not equal!")
			break
	else:
		print("Lists are identical in elements and order !")
		
