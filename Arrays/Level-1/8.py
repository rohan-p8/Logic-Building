# Find the index of the maximum element.

n = int(input("Enter no. of items: "))
list1 = []

for i in range(n):

    ele = int(input(f"Enter {i + 1} element: "))
    list1.append(ele)

print("\nEntered list is: ", list1)

maximum = max(list1)

print(f"\nIndex of Max element {maximum} is: ", list1.index(maximum))

# maximum = list1[0]

# for i in range(len(list1)):
#     if list1[i] > maximum:
#         maximum = list1[i]

# print(f"Index of max ele is: ", list1.index(maximum))
