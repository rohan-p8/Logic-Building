# Count how many elements are positive, negative, or zero.

n = int(input("Enter no. of items: "))
list1 = []

for i in range(n):

    ele = int(input(f"Enter {i + 1} element: "))
    list1.append(ele)

print("\nEntered list is: ", list1)

zero = 0
pos = 0
neg = 0

for i in range(len(list1)):

    if list1[i] > 0:
        pos += 1
    elif list1[i] < 0:
        neg += 1
    else:
        zero += 1

print(f"+ve count = {pos}, -ve count = {neg} and zero count = {zero}")

