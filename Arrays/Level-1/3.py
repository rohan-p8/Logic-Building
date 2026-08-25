# Find the average of array elements.

n = int(input("Enter no. of items: "))
l1 = []

for i in range(n):

    ele = int(input(f"Enter {i + 1} element: "))
    l1.append(ele)

print("\nEntered list is: ", l1)

sum = 0
avg = 0

for i in range(n):
    sum = sum + l1[i]
    avg = sum / len(l1)

print("Average of list elements are: ", avg)