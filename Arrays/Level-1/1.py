# Input n and take n integers into an array; print them

n = int(input("Enter no. of items: "))
l1 = []

for i in range(n):

    ele = int(input(f"Enter {i + 1} element: "))
    l1.append(ele)

print("\nThe entered list/array is: ", l1)