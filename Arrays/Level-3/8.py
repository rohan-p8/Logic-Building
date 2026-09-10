# Rotate an list by one position to the left (Manual shift).

lst = [18, 14, 8, 13, 27, 88, 45]
print("Given list: ", lst)

if len(lst) > 1:

	first = lst[0]

	for i in range(len(lst) - 1):
		lst[i] = lst[i + 1]

	lst[-1] = first

print("Rotated left by 1 position: ",lst)

