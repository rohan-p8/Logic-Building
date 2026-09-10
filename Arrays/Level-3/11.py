# Swap alternate elements (1st ↔ 2nd, 3rd ↔ 4th, etc.)

lst = [18, 14, 8, 13, 27, 88, 45]
print("Given list: ", lst)


for i in range(0, len(lst) - 1, 2):

	lst[i], lst[i + 1] = lst[i + 1], lst[i]

print("\nSwapped list: ", lst)

