# Compare two arrays — check if they contain the same elements (ignore order).

lst1 = [15,34,8,22]
lst2 = [15,34,8,22]
match = 0

if len(lst1) != len(lst2):
	print("Lists are not equal (lengths differ)!")

else:
	for item in lst1:

		for i in range(len(lst2)):
			if item == lst2[i]:
				match += 1

if match == len(lst1):
	print("Lists are equal but order is inproper")
else:
	print("Lists are not equal")


