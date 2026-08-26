#  Take n elements and print only those greater than a given value k.

n = int(input("Enter no. of elements: "))
list1 = []

for i in range(n):
    ele = int(input(f"Enter {i + 1} element: "))

    list1.append(ele)

print(f"\nGiven list is: ", list1)

k = int(input("Enter a no. to check greater no. than this: "))
greater = []

for i in range(len(list1)):
    if list1[i] > k:
        greater.append(list1[i])

print(f"\nElements Greater than {k} are: {greater}")

