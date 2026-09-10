# Rotate an array by one position to the right (using slicing).

lst = [18, 14, 8, 13, 27, 88, 45]
print("Given list: ", lst)

lst[:] = lst[-1:] + lst[:-1]

print("\nRotated right by position one: ",lst)

