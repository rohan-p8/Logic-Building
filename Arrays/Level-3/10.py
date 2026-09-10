# Rotate an array by one position to the right (Manual shift).

lst = [18, 14, 8, 13, 27, 88, 45]
print("Given list: ", lst)

if len(lst) > 1:

	last = lst[-1]

	for i in range(len(lst) - 1, 0, -1):

		lst[i] = lst[i - 1]

	lst[0] = last

print(lst)

