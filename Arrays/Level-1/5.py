# Find the minimum element in an array.

list1 = [25,85,60,34,75,99,15,2]

# print(min(list1))
# newList = sorted(list1)
# print(newList)
# print(newList[0])

min = list1[0]

for i in range(len(list1)):
    if list1[i] < min:
        min = list1[i]

print("Minimum element is: ", min)

