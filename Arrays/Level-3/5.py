# Swap the first and last elements of the list.

list1 = [18, 14, 8, 13, 27, 88, 45]
print("Given List: ", list1)

# temp = list1[0]
# list1[0] = list1[-1]
# list1[-1] = temp

list1[0], list1[-1] = list1[-1], list1[0]

print("\nAfter swap 1st and last element: ", list1)

