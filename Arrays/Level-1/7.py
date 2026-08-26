# Count how many elements are even and odd.

n = int(input("Enter no. of items: "))
list1 = []

for i in range(n):

    ele = int(input(f"Enter {i + 1} element: "))
    list1.append(ele)

print("\nEntered list is: ", list1)

even = 0
odd = 0

for i in range(len(list1)):
    if list1[i] % 2 == 0:
        even += 1
    else:
        odd += 1

print(f"\nEven count = {even}, Odd count = {odd}")

