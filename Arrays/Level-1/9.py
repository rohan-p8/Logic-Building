#  Find the index of the minimum element. 

n = int(input("Enter no. of items: "))
list1 = []

for i in range(n):

    ele = int(input(f"Enter {i + 1} element: "))
    list1.append(ele)

print("\nEntered list is: ", list1)

minimum = min(list1)

print(f"\nIndex of Min element {minimum} is: ", list1.index(minimum))
