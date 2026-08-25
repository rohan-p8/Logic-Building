# Find the sum of all elements in an array. 

n = int(input("Enter no. of items: "))
l1 = []

for i in range(n):

    ele = int(input(f"Enter {i + 1} element: "))
    l1.append(ele)

print("\nEntered list is: ", l1)

sum = 0

for i in range(n):
    sum = sum + l1[i]

print("Sum of all elemets are: ", sum)

