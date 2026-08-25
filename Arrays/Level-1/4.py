# Find the maximum element in an array

list1 = [25,85,60,34,75,99,15,2]

# print(max(list1))

# newList = sorted(list1)
# print(newList)
# print(newList[-1])
print(list1)

max = list1[0]

for i in range(len(list1)):
    if list1[i] > max:
        max = list1[i]

print("Maximum element is: ", max)

